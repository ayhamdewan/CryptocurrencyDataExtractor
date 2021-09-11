# CryptocurrencyDataExtractor
Application uses the official CoinMarketCap API to extract and organize data based on user needs. Before using this application, you must go CoinMarketCap.com and create a free developer's account to recieve your api key. After, fill in your API key for all files near the top where it says "ENTER YOUR API KEY HERE".

The crypto_data_extractor.py file is the main file.


In this application, the user will have to select an option to retrieve proper data. The list of services is shown below.

QUICK ACTIONS: 

1 - Calculate BTC and ETH dominance with total market cap and 24hr volume
2 - Full listing of cryptocurrencies
3 - Show data of a specified cryptocurrency using its ticker

ADVANCED FEATURES: 

4 - Create and set realtime audio alerts when a crypto hits a certain price
5 - Display the top 100 cryptocurrencies based on specified sorting
6 - Calculate and display future cryptocurrency values
7 - Extract and write cryptocurrency data to an excel sheet


For option 4, alerts will be notified throgh system voice and time stamped as well. The alerts will be based off the ticker symbols and prices listed on the my_alerts.csv file. There are currently some example tickers and prices in the file. Please edit your desired alerts accordingly in the csv file.

For option 7, an excel sheet will be generated called cryptocurrencies.xlsx. After the file is generated through running the service, you can open it up to find all the extracted data neatly organized


