import requests
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
import time
import csv


url = 'https://finance.yahoo.com/currencies/'
response =  requests.get(url)
#print(response.content)
soup = BeautifulSoup(response.text, "html.parser")
#test = soup.findAll('a')
test = soup.find("td",  {"data-reactid":"310"})
dt_object = datetime.now()

#print(dt_object, " : $", test.contents[0])



with open(r'//192.168.1.38/2. DATOS FUENTE/BI/Extracciones Web/exchange_rate_spot.csv', encoding="utf8", mode='w') as exchange_rate_file:
    exchange_rate_file_writer = csv.writer(exchange_rate_file, dialect='unix', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #select = '"'+str(dt_object)+'"'+',"'+str(test.contents[0])+'"'
    insert_header = ["timestamp","last_exchange_rate_spot"]
    exchange_rate_file_writer.writerow(insert_header)
    insert_row = [str(dt_object),str(test.contents[0])]
    exchange_rate_file_writer.writerow(insert_row)