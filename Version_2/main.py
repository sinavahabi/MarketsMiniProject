"""
    Program: Market Status
    Author: sina vahabi
    Copyright: 2023/02
    'Version 2.0'
"""

from MarketsMiniProject.Version_2.database import DataBase
from Classes.Colors.color import bcolors


print(bcolors.BOLD + "welcome to our program, you can choose one of these available markets and"
                     " see some momentary prices and etc. [Version 2.0]" + bcolors.ENDC)
print(bcolors.FAIL + "******************************************************************"
                     "******************************************" + bcolors.ENDC)
# After creating an object from Database class, we access class's methods, and we use them to run our program.
final = DataBase()
run = True


# Defining last function to make our program interactive with some primary options.
def running():
    global run
    user_input = 0
    user_input1 = 0
    user_input2 = 0
    print(bcolors.OKBLUE + bcolors.BOLD + "1-Crypto Currency market." + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.BOLD + "2-Local Iran market." + bcolors.ENDC)
    print(bcolors.OKGREEN + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)

    # Avoiding user input possible crashes.
    while True:
        try:
            user_input = int(input('Enter your choice: '))
            # If user intend to quit the program.
            if user_input == 0:
                print("GOODBYE.")
                run = False
            # If user intend to go back from 'cryptocurrency' market menu.
            if user_input1 == 4:
                continue
            # If user intend to go back from 'Iran Local' market menu.
            if user_input2 == 5:
                continue
            if user_input > 2:
                print(bcolors.FAIL + 'Please Either choose number 1 or 2. You can also choose \'0\''
                                     ' to exit' + bcolors.ENDC)
                continue
            if user_input < 0:
                print(bcolors.FAIL + 'Please Either choose number 1 or 2. You can also choose \'0\''
                                     ' to exit' + bcolors.ENDC)
                continue
        except:
            print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
            continue
        break

    # Checking some conditions.
    if user_input == 1:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: Bitcoin price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: Ethereum price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: BNB price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "4: Type 4 to go back through menu." + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "'Type 0 to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input1 = int(input('Enter your choice: '))
                # If user intend to quit the program.
                if user_input1 == 0:
                    print("GOODBYE.")
                    run = False
                if user_input1 > 4:
                    print(bcolors.FAIL + 'Please Either choose number 1, 2 or 3.'
                                         ' You can also choose \'0\' to exit or type 4 in order to'
                                         ' go back through menu' + bcolors.ENDC)
                    continue
                if user_input1 < 0:
                    print(bcolors.FAIL + 'Please Either choose number 1, 2 or 3. You can also choose \'0\''
                                         ' to exit or type 4 in order to go back through menu' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                continue
            break

        if user_input1 == 1:
            final.btc_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.btc_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('Bitcoin price is:', final.btc_price + '$' + ' at this moment.')
                final.bitcoin_run_count()
                final.bitcoin_run_count_reader()
                final.btc_mongo_db()
                print(bcolors.OKGREEN + "BTC Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

        if user_input1 == 2:
            final.eth_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.eth_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('Ethereum price is:', final.eth_price + '$' + ' at this moment.')
                final.ethereum_run_count()
                final.ethereum_run_count_reader()
                final.eth_mongo_db()
                print(bcolors.OKGREEN + "ETH Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

        if user_input1 == 3:
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            final.bnb_api()
            if final.btc_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('BNB price is:', final.bnb_price + '$' + ' at this moment.')
                final.bnb_run_count()
                final.bnb_run_count_reader()
                final.bnb_mongo_db()
                print(bcolors.OKGREEN + "BNB Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

    if user_input == 2:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: 18 Karat gold." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: Gold coin." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: US dollar." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "4: Total Index of Iran Stock Exchange." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "5: Type 5 to go back through menu." + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input2 = int(input('Enter your choice: '))
                # If user intend to quit the program.
                if user_input2 == 0:
                    print("GOODBYE.")
                    run = False
                if user_input2 > 5:
                    print(bcolors.FAIL + 'Please Either choose number 1, 2, 3 or 4.'
                                         ' You can also choose \'0\' to exit or type 5 '
                                         'in order to go back through menu' + bcolors.ENDC)
                    continue
                if user_input2 < 0:
                    print(bcolors.FAIL + 'Please Either choose number 1, 2,3 or 4 . You can also choose \'0\''
                                         ' to exit or type 5 in order to go back through menu' + bcolors.ENDC)
                    continue
            except:
                print(bcolors.FAIL + 'You can only enter an integer number.' + bcolors.ENDC)
                continue
            break
        if user_input2 == 1:
            final.gold_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.gold_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('18 Karat Gold price in Iran is:', final.gold_price, 'Rials at the moment.')
                final.gold_run_count()
                final.gold_run_count_reader()
                final.gold_mongo_db()
                print(bcolors.OKGREEN + "18 Karat Gold Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

        if user_input2 == 2:
            final.gold_coin_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.gold_coin_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('Gold Coin price in Iran is:', final.gold_coin_price, 'Rials at the moment.')
                final.gold_coin_run_count()
                final.gold_coin_run_count_reader()
                final.gold_coin_mongo_db()
                print(bcolors.OKGREEN + "Gold Coin Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

        if user_input2 == 3:
            final.dollar_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.dollar_price == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('US Dollar price in Iran is:', final.dollar_price, 'Rials at the moment.')
                final.dollar_run_count()
                final.dollar_run_count_reader()
                final.dollar_mongo_db()
                print(bcolors.OKGREEN + "US Dollar Momentary price has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)

        if user_input2 == 4:
            final.stock_market_api()
            # If returned value from web was empty by the try except method from 'api.py' module, then show this message
            if final.stock_market_amount == '':
                print(bcolors.FAIL + 'we\'re not able to show the results at the moment,'
                                     ' please try again later!' + bcolors.ENDC)
            else:
                print('Total Index of Iran Stock Exchange is:', final.stock_market_amount, 'Million.')
                final.stock_market_run_count()
                final.stock_market_run_count_reader()
                final.stock_market_mongo_db()
                print(bcolors.OKGREEN + "Total Index of Iran Stock Exchange has been inserted"
                                        " into the database successfully.\n" + bcolors.ENDC)


# Calling last function in a while loop.
while run:
    running()
