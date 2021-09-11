# Returns data of a certain ticker

# Imports
import requests
import json

def quotes():
    # Setting our local currency and its symbol
    local_currency = 'USD'
    local_symbol = '$'

    # Personal API key
    api_key = 'ENTER YOUR API KEY HERE'
    # Formatting API into dictionary
    headers = {'X-CMC_PRO_API_KEY': api_key}

    base_url = 'https://pro-api.coinmarketcap.com'

    # Ask for user input
    symbol = input('Enter the ticker symbol of a cryptocurrency: ').upper()

    # Endpoints = something added to the end of the base url
    # First parameter starts with ? before input
    # Second parameter and onwards start with & before input
    global_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

    # Making request
    request = requests.get(global_url, headers = headers)
    results = request.json()

    # print(json.dumps(results, sort_keys = True, indent = 4))

    # Accesses ticker symbol data
    data = results["data"]
    currency = data[symbol]

    name = currency["name"]

    price = currency["quote"][local_currency]["price"]
    percent_change_24h = currency["quote"][local_currency]["percent_change_24h"]
    market_cap = currency["quote"][local_currency]["market_cap"]

    # Round values
    price = round(price, 2)
    percent_change_24h = round(percent_change_24h, 2)
    market_cap = round(market_cap, 2)

    # Formatting in commas
    price_str = local_symbol + '{:,}'.format(price)
    percent_change_24h_str = '{:,}'.format(percent_change_24h) + "%"
    market_cap_str = local_symbol + '{:,}'.format(market_cap)

    # Printing out data
    print(name + ' (' + symbol + ')')
    print('Price ' + price_str)
    print('24H Change: ' + percent_change_24h_str)
    print('Market Cap: ' + market_cap_str)
    print()
