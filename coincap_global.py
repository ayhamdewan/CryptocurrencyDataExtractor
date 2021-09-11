# Returns BTC and ETH information only

# Imports
import requests
import json

def dominance():
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

    # Make request
    request = requests.get(global_url, headers = headers)
    results = request.json()

    # print(json.dumps(results, sort_keys = True, indent = 4))

    # Accesses full data level
    data = results["data"]

    # Store wanted data
    btc_dominance = data["btc_dominance"]
    eth_dominance = data["eth_dominance"]
    total_market_cap = data["quote"][local_currency]["total_market_cap"]
    total_volume_24h = data["quote"][local_currency]["total_volume_24h"]

    # Round values
    btc_dominance = round(btc_dominance, 2)
    eth_dominance = round(eth_dominance, 2)
    total_market_cap = round(total_market_cap, 2)
    total_volume_24h = round(total_volume_24h, 2)

    # Formatting in commas
    total_market_cap_str = local_symbol + '{:,}'.format(total_market_cap)
    total_volume_24h_str = local_symbol + '{:,}'.format(total_volume_24h)

    # Printing out data
    print()
    print('The global market cap for all cryptocurrencies is ' + total_market_cap_str + '.')
    print('The global 24hr volume is ' + total_volume_24h_str + '.')
    print()
    print(f'Bitcoin (BTC) makes up {btc_dominance}% of the global total_market_cap')
    print(f'Ethereum (ETH) makes up  {eth_dominance}% of the global market cap.')
