import requests
import bs4
import csv

with open('GITHUB/Content_Main.csv', 'r') as file:
    reader = csv.reader(file)
    rows= list(file)
    csv_url=(rows[0]).strip()
response=requests.get(csv_url)
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted=bs.prettify()
with open("GITHUB/website.html","w+") as f:
    f.write(formatted)