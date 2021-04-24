import requests
import csv
import time
import json
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import os
import datetime  
from mailjet_rest import Client
import mysql.connector 



toaster = ToastNotifier()
stored_price=""

#This block reads the stored data form CSV file
with open('GITHUB/filename.csv', 'r') as file:
    reader = csv.reader(file)
    rows= list(file)
    csv_url=(rows[0])
    csv_email=str(rows[1]).strip()
    csv_number=(rows[2])
    csv_time=(rows[3])
print(csv_email)


#This function scrapes data form website acoording to the file which was read above
def extract_data():
    global URL
    URL= csv_url
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    global title
    title = soup.find(id="productTitle").get_text(strip=True)
    print(title.strip())
    try:
        price = soup.find(id='priceblock_ourprice').get_text(strip=True)
    except:
            #this is works if 'id' is changed. 
      try:
            price=soup.find(id='priceblock_dealprice').get_text()
      except:
            price=''
    global extracted_price
    extracted_price = int(price[1:12].replace(',','').replace('.00',''))
    print(extracted_price)
    global msg
    msg=str("PRICE DROPPED ! for product: " +title.strip()+ "    DROPPED PRICE:  ₹" +str(extracted_price))
    msg2=str(title.strip()+ " Cr. Price:₹" +str(extracted_price))
    print(msg2)


def store_csv():
        #Mention a path below to store scraped price
        with open('GITHUB/filename.csv', mode='w') as price_file:
            price_file.write(str(extracted_price))


def read_csv():
    #Mention the above mentioned path here
    with open('projectV1/amazon_price.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            global stored_price
            stored_price=int(row[0])
read_csv()
print(stored_price)


#This function stores data in database to be viewed in the log gui based window
#Mention your database name, user, password and host
#create a table which resembles the following
def store_db():
        mydb = mysql.connector.connect(user='default', password='default',host='localhost',database='scraper')
        cur=mydb.cursor()
        s="INSERT INTO scrpdata(scraper,product_title,usual_price,dropped_price,time) VALUES (%s,%s,%s,%s,%s);"
        t1=('Amazon_Scraper',title,stored_price,extracted_price,current_time)
        cur.execute(s,t1)
        mydb.commit()
        print("data stored in database")


def toast_noti():
     toaster.show_toast("PRICE SCRAPER",
     msg,
     icon_path=None,
     duration=7,
     threaded=True)
     toaster.notification_active
     print("price lower than extracted price")
#This block sends user a drop alert on specified mail
#You need to create a  FREE account on MailJet.com to use this API
def send_mail():
    api_key = 'Mention your API key here'
    api_secret = 'Mention your secret API key here'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "mention your sender mail here",
            "Name": "PRICE_SCRAPER"
        },
        "To": [
            {
            "Email": csv_email,
            "Name": "USER"
            }
        ],
        "Subject": msg,
        "TextPart": URL,
        #"HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
        #"CustomID": "AppGettingStartedTest"
        }
    ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())


def send_sms():
    resp = requests.post('https://textbelt.com/text', {
        'phone': csv_number,
        'message': 'price dropped for a certain product pls check your mail',
        'key': 'textbelt',
    })
    print(resp.json())




def checker():
    while(True):
      print("running in while")
      extract_data()
      time.sleep(10)
      if(extracted_price == stored_price):
        toast_noti()
        send_mail()
        #send_sms()
        global current_time
        current_time = datetime.datetime.now() 
        print (current_time) 
        #store_db() 
        break


def testing():
    if(not stored_price):
        print("extracting data")
        extract_data()
        store_csv()
        read_csv()
        checker()
    else:
        print("checking data")
        read_csv()
        print(stored_price)
        checker()
        
    

testing()
