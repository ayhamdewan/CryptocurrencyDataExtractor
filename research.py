# Imports
import math
import json
import locale
import requests
from prettytable import PrettyTable

def research():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Setting our local currency and its symbol
    local_currency = 'USD'
    local_symbol = '$'

    # Personal API key
    api_key = 'ENTER YOUR API KEY HERE'
    # Formatting API into dictionary
    headers = {'X-CMC_PRO_API_KEY': api_key}

    base_url = 'https://pro-api.coinmarketcap.com'

    # Endpoints = something added to the end of the base url
    global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

    request = requests.get(global_url, headers = headers)
    results = request.json()

    # print(json.dumps(results, sort_keys = True, indent = 4))

    # Accesses full data level
    data = results["data"]

    # Store wanted data
    total_market_cap = data["quote"][local_currency]["total_market_cap"]
    total_market_cap_str = '{:,}'.format(total_market_cap)

    # Create table
    table = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Price', '10.9T (Gold)', '35.2T (Narrow Money)', '89.5T (Stock Markets)'])

    listings_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

    # Make request
    request = requests.get(listings_url, headers=headers)
    results = request.json()

    data = results["data"]

    # Extract data for each currency
    for currency in data:
        name = currency["name"]
        ticker = currency["symbol"]

        market_cap = currency["quote"][local_currency]["market_cap"]
        percentage_of_global_cap = float(market_cap) / float(total_market_cap)
        price = currency["quote"][local_currency]["price"]
        available_supply = currency["total_supply"]

        # Calculations
        gold_price = 10900000000000 * percentage_of_global_cap / available_supply
        narrow_money_price = 35200000000000 * percentage_of_global_cap / available_supply
        stock_market_price = 89500000000000 * percentage_of_global_cap / available_supply

        # Formatting values
        percentage_of_global_cap_str = str(round(percentage_of_global_cap * 100, 2)) + '%'
        price_str = local_symbol + '{:,}'.format(round(price, 2))
        gold_price_str = local_symbol + '{:,}'.format(round(gold_price, 2))
        narrow_money__price_string = local_symbol + '{:,}'.format(round(narrow_money_price, 2))
        stock_market_price_str = local_symbol + '{:,}'.format(round(stock_market_price, 2))

        # Adding to table
        table.add_row([name, ticker, percentage_of_global_cap_str, price_str, gold_price_str, narrow_money__price_string, stock_market_price_str])

    # Display table
    print()
    print(table)
