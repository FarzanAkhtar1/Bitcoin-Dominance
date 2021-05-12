import json
import requests
import time
from datetime import datetime
import csv

response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false')
#print(response)
response = response.json()
BTCCap = 0
altCap = 0
for x in response:
    #print(x['id'])
    if x['id'] == "bitcoin":
        BTCCap = x['market_cap']
        altCap = altCap + x['market_cap']
    else:
        altCap = altCap + x['market_cap']
        
current_time = datetime.now().strftime("%d-%m-%Y")
with open("BTCDominance.csv", mode='a+', newline ="") as datawriter:
    datawriter = csv.writer(datawriter, delimiter=",")
    datawriter.writerow([current_time,"{:.2f}".format((BTCCap/altCap)*100)])