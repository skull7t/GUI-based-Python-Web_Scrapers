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

with open('GITHUB/YahooFin_System.csv', 'r') as file:
    reader = csv.reader(file)
    rows= list(file)
    stock_name=str(rows[0]).strip()
print(stock_name)

with open('GITHUB/YahooFin_User.csv', 'r') as file:
    reader = csv.reader(file)
    rows= list(file)
    csv_price=(rows[0]).strip()
    csv_number=(rows[1]).strip()
    csv_email=(rows[2]).strip()
print(csv_price)
print(csv_email)
print(csv_number)

def StockPrice_extractor():
    global url1
    url1='https://in.finance.yahoo.com/quote/'+stock_name+'.NS?p='+stock_name+'.NS&.tsrc=fin-srch'
    print(url1)
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    page=requests.get(url1,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    price=(soup.find_all('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].text)
    global converted_p
    converted_p = price.replace(',','').replace('.00','')
    title=(soup.find('h1',{'class':'D(ib) Fz(18px)'}).text)
    global msg
    msg=str("PRICE ALERT for stock: " +title.strip()+ "    CURRENT PRICE: ₹" +str(converted_p))

    print(title)
    print(converted_p)




def toast_noti():
    #if(extracted_price == stored_price):
     toaster.show_toast("PRICE SCRAPER",
     msg,
     icon_path=None,
     duration=7,
     threaded=True)
     toaster.notification_active
     print("price matched with stock price")

def send_mail():
    api_key = 'YOUR API KEY'
    api_secret = 'YOUR API KEY'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
        {
        "From": {
            "Email": "SENDER'S EMAIL",
            "Name": "PRICE_SCRAPER"
        },
        "To": [
            {
            "Email": csv_email,
            "Name": "USER"
            }
        ],
        "Subject": msg,
        "TextPart": url1,
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
        'message': 'price alert for stock'+stock_name+'current price'+converted_p,
        'key': 'textbelt',
    })
    print(resp.json())

def checker():
    while(True):
        print("running in while")
        StockPrice_extractor()
        time.sleep(2)
        if(converted_p == csv_price):
            toast_noti()
            send_mail()
            #send_sms()
            global current_time
            current_time = datetime.datetime.now() 
            print (current_time) 
            #store_db() 
            break


def testing():
    if(not csv_price):
        print("No available data")
    else:
        print("checking data")
        print("user stored price",csv_price)
        checker()

testing()