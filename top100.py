#Imports
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

def top_100():
    # Setting our local currency and its symbol
    local_currency = 'USD'
    local_symbol = '$'

    # Personal API key
    api_key = 'ENTER YOUR API KEY HERE'
    # Formatting API into dictionary
    headers = {'X-CMC_PRO_API_KEY': api_key}

    base_url = 'https://pro-api.coinmarketcap.com'

    # Print out menu
    print()
    print("CoinMarketCap Explorer Menu")
    print()
    print("1 - Top 100 sorted by market cap")
    print("2 - Top 100 sorted by 24hr change")
    print("3 - Top 100 sorted by 24hr volume")
    print("0 - Exit")
    print()

    # Code in error handling if not 1, 2, or 3
    choice = input("What is your choice? (choose 1, 2, or 3): ")

    # Use sort as an api parameter
    sort = ""
    if choice == '1':
        sort = 'market_cap'
    elif choice == '2':
        sort = 'percent_change_24h'
    elif choice == '3':
        sort = 'volume_24h'
    elif choice == '0':
        exit(0)

    quote_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency + '&sort=' + sort

    # Make request
    request = requests.get(quote_url, headers = headers)
    results = request.json()

    # print(json.dumps(results, sort_keys = True, indent = 4))

    data = results["data"]

    # Set table headers
    table = PrettyTable(['Ranking', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])

    # Extract data from each of the top 100 cryptocurrencies
    ranking = 0
    for currency in data:
        ranking += 1
        name = currency["name"]
        symbol = currency["symbol"]

        quote = currency["quote"][local_currency]
        market_cap = quote["market_cap"]
        hour_change = quote["percent_change_1h"]
        day_change = quote["percent_change_24h"]
        week_change = quote["percent_change_7d"]
        price = quote["price"]
        volume = quote["volume_24h"]

        # Rounding values when present
        if hour_change is not None:
            hour_change = round(hour_change, 2)
            if hour_change > 0:
                hour_change = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL
        if day_change is not None:
            day_change = round(day_change, 2)
            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL
        if week_change is not None:
            week_change = round(week_change, 2)
            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

        # Formatting in commas when neccessary
        if volume is not None:
            volume_str = '{:,}'.format(round(volume, 2))
        if market_cap is not None:
            market_cap_str = '{:,}'.format(round(market_cap, 2))
        price_str = '{:,}'.format(round(price, 2))

        # Adding to table
        table.add_row([ranking, name + ' (' + symbol + ')',
                      local_symbol + price_str,
                      local_symbol + market_cap_str,
                      local_symbol + volume_str,
                      str(hour_change),
                      str(day_change),
                      str(week_change)])

    # Print table
    print()
    print(table)
    print()
