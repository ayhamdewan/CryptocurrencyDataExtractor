# Imports
import requests
import json
import xlsxwriter

def excel_writer():
    # Setting our local currency and its symbol
    local_currency = 'USD'
    local_symbol = '$'

    # Personal API key
    api_key = 'ENTER YOUR API KEY HERE'
    # Formatting API into dictionary
    headers = {'X-CMC_PRO_API_KEY': api_key}

    base_url = 'https://pro-api.coinmarketcap.com'

    # Creating a new excel workbook and adding a new worksheet
    crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
    crypto_sheet = crypto_workbook.add_worksheet()

    # Creating the headers
    crypto_sheet.write('A1', 'Name')
    crypto_sheet.write('B1', 'Symbol')
    crypto_sheet.write('C1', 'Market Cap')
    crypto_sheet.write('D1', 'Price')
    crypto_sheet.write('E1', '24H Volume')
    crypto_sheet.write('F1', 'Hour Change')
    crypto_sheet.write('G1', 'Day Change')
    crypto_sheet.write('H1', 'Week Change')

    start = 1
    row = 1

    for i in range(10):
        listings_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency + '&start=' + str(start)

        # Make request
        request = requests.get(listings_url, headers=headers)
        results = request.json()

        data = results["data"]

        # Extract data for each currency
        for currency in data:
            name = currency["name"]
            symbol = currency["symbol"]

            quote = currency["quote"][local_currency]
            market_cap = quote["market_cap"]
            hour_change = quote["percent_change_1h"]
            day_change = quote["percent_change_24h"]
            week_change = quote["percent_change_7d"]
            price = quote["price"]
            volume = quote["volume_24h"]

            # Formatting values
            volume_str = '{:,}'.format(volume)
            market_cap_str = '{:,}'.format(market_cap)

            # Write values in cells respectively
            crypto_sheet.write(row, 0, name)
            crypto_sheet.write(row, 1, symbol)
            crypto_sheet.write(row, 2, local_symbol + market_cap_str)
            crypto_sheet.write(row, 3, local_symbol + str(price))
            crypto_sheet.write(row, 4, local_symbol + volume_str)
            crypto_sheet.write(row, 5, str(hour_change) + '%')
            crypto_sheet.write(row, 6, str(day_change) + '%')
            crypto_sheet.write(row, 7, str(week_change) + '%')

            # Moving down to the next row after each cryptocurrency
            row += 1

        start += 100

         # print(json.dumps(data, sort_keys = True, indent = 4))

    # Save and close workbook
    crypto_workbook.close()
    print("Excel workbook updated")
