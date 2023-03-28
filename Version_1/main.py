"""
    Program: Market Status
    Author: sina vahabi
    Copyright: 2023/02
    'Version 1.0'
"""

from MarketsMiniProject.Version_1.api import *
from Classes.Colors.color import bcolors


# After importing all the essential packages and modules that we need, our program is ready to begin.
run = True
print(bcolors.BOLD + "welcome to our program, "
      "you can choose one of these available markets and see some momentary prices and etc. [Version 1.0]"
      + bcolors.ENDC)
print(bcolors.OKGREEN + "******************************************************************"
                        "******************************************" + bcolors.ENDC)


# Defining last function to make our program interactive with some primary options.
def result_func():
    global run
    user_input = 0
    user_input1 = 0
    user_input2 = 0
    print(bcolors.OKBLUE + bcolors.BOLD + "1-Crypto Currency market." + bcolors.ENDC)
    print(bcolors.OKBLUE + bcolors.BOLD + "2-Local(Iran) market." + bcolors.ENDC)
    print(bcolors.OKGREEN + bcolors.BOLD + "'Type 0 number to exit.'" + bcolors.ENDC)

    while True:
        try:
            user_input = int(input('Enter your choice: '))
            if user_input == 0:
                print("GOODBYE.")
                run = False
            if user_input1 == 4:
                continue
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

    if user_input == 1:
        print(bcolors.OKBLUE + bcolors.BOLD + "1: Bitcoin price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "2: Ethereum price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "3: BNB price." + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "4: Type 4 to go back through menu." + bcolors.ENDC)
        print(bcolors.OKGREEN + bcolors.BOLD + "'Type 0 to exit.'" + bcolors.ENDC)
        while True:
            try:
                user_input1 = int(input('Enter your choice: '))
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
            btc_func()
        if user_input1 == 2:
            eth_func()
        if user_input1 == 3:
            bnb_func()

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
                if user_input2 == 0:
                    print("GOODBYE.")
                    run = False
                if user_input2 > 5:
                    print(bcolors.FAIL + 'Please Either choose number 1, 2, 3 or 4.'
                                         ' You can also choose \'0\' to exit or type 5 in order to go back through menu' + bcolors.ENDC)
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
            gold_func()
        if user_input2 == 2:
            gold_coin_func()
        if user_input2 == 3:
            us_dollar_func()
        if user_input2 == 4:
            stock_market_func()


# Calling last function in a while loop.
while run:
    result_func()
