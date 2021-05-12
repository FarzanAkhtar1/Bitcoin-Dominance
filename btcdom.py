import csv
import json
import time
from datetime import datetime

import requests

#gets data from coingecko
response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false')
response = response.json()

#initialises variables
BTCCap = 0
altCap = 0
current_time = datetime.now().strftime("%d-%m-%Y")
#current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


#iterates through response
for x in response:
    #print(x['id'])
    if x['id'] == "bitcoin": #adds bitcoin market cap to BTCCap and altCap
        BTCCap = x['market_cap']
        altCap = altCap + x['market_cap']
    else: #adds any altcoin market cap to altCap
        altCap = altCap + x['market_cap']
        
with open("BTCDominance.csv", mode='a+', newline ="") as datawriter: #writes the data to a CSV BTCDominance, will generate the file if it does not exist.
    datawriter = csv.writer(datawriter, delimiter=",")
    datawriter.writerow([current_time,"{:.2f}".format((BTCCap/altCap)*100)]) #writes bitcoin dominance out of 100 to 2dp
