# Imports
import os
import csv
import sys
import json
import time
import requests
from datetime import datetime

def alert_system():
    # Setting our local currency and its symbol
    local_currency = 'USD'
    local_symbol = '$'

    # Personal API key
    api_key = 'ENTER YOUR API KEY HERE'
    # Formatting API into dictionary
    headers = {'X-CMC_PRO_API_KEY': api_key}

    base_url = 'https://pro-api.coinmarketcap.com'

    print()
    print("ALERTS TRACKING...")
    print()

    # Alert message
    def alert():
        os.system('say ALERT ALERT ALERT')
        os.system('say ' + name + ' hit ' + amount)
        sys.stdout.flush()

    # Add to list if symobl has been alerted
    alerted_symbols = []

    while True:
        # Reading data from csv file
        with open("my_alerts.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                # Handle unwanted intialized characters on Mac
                if '\ufeff' in line[0]:
                    line[0] = line[0][1:].upper()
                else:
                    line[0] = line[0].upper()

                symbol = line[0].upper()
                amount = line[1]

                # Making request
                quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol
                request = requests.get(quote_url, headers=headers)
                results = request.json()

                # Extract data from API
                currency = results["data"][symbol]
                name = currency["name"]
                price = currency["quote"][local_currency]["price"]

                if float(price) >= float(amount) and symbol not in alerted_symbols:
                    # Alert activated. Repeats twice
                    alert()
                    alert()

                    # Time logs when alert was hit and prints it
                    now = datetime.now()
                    current_time = now.strftime("%I:%M%p")
                    print(name + ' hit ' + amount + ' at ' + current_time + '!')

                    # Adds ticker symbol to alerted list
                    alerted_symbols.append(symbol)

        print('...')
        # Checks for alerts every 10 seconds
        time.sleep(10)
