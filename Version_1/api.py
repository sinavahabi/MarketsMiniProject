# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install pymongo
# pip install bs4
# pip install requests

from RunCount.RunCountBitcoin.main import bitcoin_run_count
from RunCount.RunCountEthereum.main import ethereum_run_count
from RunCount.RunCountBNB.main import bnb_run_count
from RunCount.RunCountGold.main import gold_run_count
from RunCount.RunCountGoldCoin.main import gold_coin_run_count
from RunCount.RunCountDollar.main import dollar_run_count
from RunCount.RunCountStockMarket.main import stock_market_run_count
from Classes.Colors.color import bcolors
from pymongo import MongoClient
from bs4 import BeautifulSoup
import datetime
import requests
import re


# After importing all the essential packages and modules that we need, our program is ready to begin.
btc = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
eth = 'https://coinmarketcap.com/currencies/ethereum/'
bnb = 'https://coinmarketcap.com/currencies/bnb/'
gold = 'https://www.tgju.org/profile/geram18'
gold_coin = 'https://www.tgju.org/profile/sekee'
us_dollar = 'https://www.tgju.org/profile/crypto-tether'
stock_market = 'https://www.shakhesban.com/markets/index/%D8%B4-%DA%A9%D9%84-%D8%A8%D9%88%D8%B1%D8%B3'
current_time = datetime.datetime.now()
date = str(current_time)

'''
    We almost use an exact structure for all functions, and by defining each desired element function we have 3 stages.
    First stage is to get and read desired data (Bitcoin price for example) from web.
    Second stage is Counter part which counts every single time that program has been running and data has been returned
    to data base.
    Third stage is DataBase part. After getting desired data we send it to database(MongoDB) immediately.  
    By using regex we remove every unessential other stuff that we get from web by the way.      
'''


# Defining functions.
def btc_func():
    # Bitcoin API.
    response_btc = requests.get(btc)
    res_btc = response_btc.text
    soup = BeautifulSoup(res_btc, "html.parser")
    result_btc = soup.find('div', attrs={'class': 'priceValue'})
    final_result_btc = result_btc.text
    btc_price = re.sub(r'\$', '', final_result_btc)
    print('Bitcoin price is:', btc_price + '$' + ' at this moment.')
    # Counting run times.
    bitcoin_run_count()
    # By reading count from txt file we can insert it to DataBase.
    btc_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountBitcoin/bitcoin_count.txt", 'r')
    run_count_btc = btc_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    crypto_currency = db.crypto_currency
    price = crypto_currency.insert_one({"name": "Bitcoin", "price": btc_price + ' $',
                                        "Run Count": run_count_btc, "date": date[:16]})
    print(bcolors.OKGREEN + "BTC Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def eth_func():
    # Ethereum API.
    response_eth = requests.get(eth)
    res_eth = response_eth.text
    soup = BeautifulSoup(res_eth, "html.parser")
    result_eth = soup.find('div', attrs={'class': 'priceValue'})
    final_result_eth = result_eth.text
    eth_price = re.sub(r'\$', '', final_result_eth)
    print('Ethereum price is:', eth_price + '$' + ' at this moment.')
    # Counting run times.
    ethereum_run_count()
    # By reading count from txt file we can insert it to DataBase.
    eth_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountEthereum/ethereum_count.txt", 'r')
    run_count_eth = eth_file.read()

    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    crypto_currency = db.crypto_currency
    price = crypto_currency.insert_one({"name": "Ethereum", "price": eth_price + ' $',
                                        "Run Count": run_count_eth, "date": date[:16]})
    print(bcolors.OKGREEN + "ETH Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def bnb_func():
    # BNB API.
    response_bnb = requests.get(bnb)
    res_bnb = response_bnb.text
    soup = BeautifulSoup(res_bnb, "html.parser")
    result_bnb = soup.find('div', attrs={'class': 'priceValue'})
    final_result_bnb = result_bnb.text
    bnb_price = re.sub(r'\$', '', final_result_bnb)
    print('BNB price is:', bnb_price + '$' + ' at this moment.')
    # Counting run times.
    bnb_run_count()
    # By reading count from txt file we can insert it to DataBase.
    bnb_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountBNB/bnb_count.txt", 'r')
    run_count_bnb = bnb_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    crypto_currency = db.crypto_currency
    price = crypto_currency.insert_one({"name": "BNB", "price": bnb_price + ' $',
                                        "Run Count": run_count_bnb, "date": date[:16]})
    print(bcolors.OKGREEN + "BNB Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def gold_func():
    # 18 Karat Gold API.
    response_gold = requests.get(gold)
    res_gold = response_gold.text
    soup = BeautifulSoup(res_gold, "html.parser")
    result_gold = soup.find('td', attrs={'class': 'text-left'})
    final_result_gold = result_gold.text
    gold_price = re.sub(r'[^,\d]', '', final_result_gold)
    print('18 Karat Gold price in Iran is:', gold_price, 'Rials at the moment.')
    # Counting run times.
    gold_run_count()
    # By reading count from txt file we can insert it to DataBase.
    gold_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountGold/gold_count.txt", 'r')
    run_count_gold = gold_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    iran_local = db.iran_local
    price = iran_local.insert_one({"name": "18 Karat Gold", "price": gold_price + ' Rials',
                                   "Run Count": run_count_gold, "date": date[:16]})
    print(bcolors.OKGREEN + "18 Karat Gold Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def gold_coin_func():
    # Gold Coin API.
    response_gold_coin = requests.get(gold_coin)
    res_gold_coin = response_gold_coin.text
    soup = BeautifulSoup(res_gold_coin, "html.parser")
    result_gold_coin = soup.find('td', attrs={'class': 'text-left'})
    final_result_gold_coin = result_gold_coin.text
    gold_coin_price = re.sub(r'[^,\d]', '', final_result_gold_coin)
    print('Gold Coin price in Iran is:', gold_coin_price, 'Rials at the moment.')
    # Counting run times.
    gold_coin_run_count()
    # By reading count from txt file we can insert it to DataBase.
    gold_coin_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountGoldCoin/"
                          "gold_coin_count.txt", 'r')
    run_count_gold_coin = gold_coin_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    iran_local = db.iran_local
    price = iran_local.insert_one({"name": "Gold Coin", "price": gold_coin_price + ' Rials',
                                   "Run Count": run_count_gold_coin, "date": date[:16]})
    print(bcolors.OKGREEN + "Gold Coin Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def us_dollar_func():
    # US Dollar API.
    response_dollar = requests.get(us_dollar)
    res_dollar = response_dollar.text
    soup = BeautifulSoup(res_dollar, "html.parser")
    result_dollar = soup.find_all('td', attrs={'class': 'text-left'})
    final_result_dollar = result_dollar[1].text
    dollar_price = re.sub(r'[^,\d]', '', final_result_dollar)
    print('US Dollar price in Iran is:', dollar_price, 'Rials at the moment.')
    # Counting run times.
    dollar_run_count()
    # By reading count from txt file we can insert it to DataBase.
    dollar_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountDollar/dollar_count.txt", 'r')
    run_count_dollar = dollar_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    iran_local = db.iran_local
    price = iran_local.insert_one({"name": "US Dollar", "price": dollar_price + ' Rials',
                                   "Run Count": run_count_dollar, "date": date[:16]})
    print(bcolors.OKGREEN + "US Dollar Momentary price has been inserted into the database successfully.\n" + bcolors.ENDC)


def stock_market_func():
    # Total Index of Iran Stock Exchange API.
    response_stock_market = requests.get(stock_market)
    res_stock_market = response_stock_market.text
    soup = BeautifulSoup(res_stock_market, "html.parser")
    result_stock_market = soup.find('span', attrs={'dir': 'ltr'})
    final_result_market = result_stock_market.text
    stock_market_amount = re.sub(r'[^0-9.]', '', final_result_market)
    print('Total Index of Iran Stock Exchange is:', stock_market_amount, 'Million.')
    # Counting run times.
    stock_market_run_count()
    # By reading count from txt file we can insert it to DataBase.
    stock_market_file = open("F:/Workspace/PycharmProjects/MarketsMiniProject/RunCount/RunCountStockMarket/"
                             "stock_market_count.txt", 'r')
    run_count_stock_market = stock_market_file.read()
    # Connecting to DataBase.
    mongo_client = MongoClient("localhost", 27017)
    db = mongo_client.market
    iran_local = db.iran_local
    price = iran_local.insert_one({"name": "Total Index of Iran Stock Exchange",
                                   "amount": stock_market_amount + ' Million',
                                   "Run Count": run_count_stock_market, "date": date[:16]})
    print(bcolors.OKGREEN + "Total Index of Iran Stock Exchange has been inserted into the database successfully.\n"
          + bcolors.ENDC)
