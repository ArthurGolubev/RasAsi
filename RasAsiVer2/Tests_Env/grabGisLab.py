from bs4 import BeautifulSoup
import requests
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet
from datetime import datetime

link ='http://gis-lab.info'
html = requests.get('http://gis-lab.info/qa.html').text

soup = BeautifulSoup(html, 'html.parser')
p = soup.find('div', class_="articles-block")
k = p.find_all('ol')
print(len(k))

transaction = []
counter = 0
date = datetime.now().strftime('%d.%m.%Y')
for i in k:
    soup = i.find_all('li')
    print(len(soup))
    for li in soup:
        link_= li.find('a').get('href')
        counter += 1
        transaction.append([date, link+link_, 0])


print(counter)
print(transaction)
GoogleSpreadsheet().append_spreadsheets_values(values=transaction,
                                               spreadsheet_id='1DvY6qzp32qP_BNTFU2opXlfQ0lpnjs1MnGZ7LWRJIbw',
                                               range_name='Лист1')