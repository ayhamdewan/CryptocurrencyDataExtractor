# Created by: Ayham Dewan

# Imports
from colorama import Fore, Back, Style
from coincap_global import dominance
from coincap_listings import listings
from coincap_quotes import quotes
from alerts import alert_system
from top100 import top_100
from research import research
from excel_writer import excel_writer


# Divider to organize displayed sections
def divider():
    print()
    print(Fore.MAGENTA + '*' * 100 + Style.RESET_ALL)
    print()

options = (1,2,3,4,5,6,7)
quit_option = ''

# Loop that continues/quits the program
while quit_option != 'q':
    # Welcoming the user
    divider()
    print(Fore.GREEN + "WELCOME TO THE CRYPTOCURRENCY DATA EXTRACTOR!")
    divider()
    # Quick services
    print(Fore.YELLOW + "QUICK ACTIONS: ")
    print()
    print("1 - Calculate BTC and ETH dominance with total market cap and 24hr volume")
    print("2 - Full listing of cryptocurrencies")
    print("3 - Show data of a specified cryptocurrency using its ticker")
    divider()
    # Advanced services
    print(Fore.CYAN + "ADVANCED FEATURES: ")
    print()
    print("4 - Create and set realtime audio alerts when a crypto hits a certain price")
    print("5 - Display the top 100 cryptocurrencies based on specified sorting")
    print("6 - Calculate and display future cryptocurrency values")
    print("7 - Extract and write cryptocurrency data to an excel sheet" + Style.RESET_ALL)
    print()
    choice = 0
    while choice not in options:
        print("\nInvalid option. Please try again.")
        choice = int(input("Please pick an option: 1, 2, 3, 4, 5, 6, 7\n"))
    divider()

    # Decision making based on user request
    if choice == 1:
        dominance()
    elif choice == 2:
        listings()
    elif choice == 3:
        quotes()
    elif choice == 4:
        alert_system()
    elif choice == 5:
        top_100()
    elif choice == 6:
        research()
    elif choice == 7:
        excel_writer()

    # Ask if user wants to quit or go back to services menu
    print()
    quit_option = input("Enter Q to quit the application or any other key to go back to the services menu: ").casefold()
