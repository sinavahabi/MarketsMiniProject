# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install pymongo
# pip install jdatetime

# Importing all the essential Packages, API and Counter classes.
from MarketsMiniProject.Version_2.api import API
from MarketsMiniProject.Version_2.counter import Counter
from pymongo import MongoClient
import datetime
import jdatetime


'''
    By Instantiating DataBase class in third stage and After getting desired data, we send it to 
    database(MongoDB) immediately. 
    Each method has been defined to insert a specific data (document) into Mongo DateBase.
    By DataBase class inheritance from API and Counter class we have access to received data from web and program 
    run counter. For example Bitcoin price, program run counter and current date are inserted into DataBase each time 
    we choose to receive Bitcoin price and etc.
'''


class DataBase(API, Counter):

    def btc_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: crypto_currency.
        crypto_currency = db.crypto_currency
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting Bitcoin Price, Current time and Run Count.
        price = crypto_currency.insert_one({"name": "Bitcoin", "price": self.btc_price + ' $', "Run Count":
                                            self.run_count_btc, "date": date[:16], "jalali date": jdate[:16]})

    def eth_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: crypto_currency.
        crypto_currency = db.crypto_currency
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting Ethereum Price, Current time and Run Count.
        price = crypto_currency.insert_one({"name": "Ethereum", "price": self.eth_price + ' $', "Run Count":
                                            self.run_count_eth, "date": date[:16], "jalali date": jdate[:16]})

    def bnb_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: crypto_currency.
        crypto_currency = db.crypto_currency
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting BNB Price, Current time and Run Count.
        price = crypto_currency.insert_one({"name": "BNB", "price": self.bnb_price + ' $', "Run Count":
                                            self.run_count_bnb, "date": date[:16], "jalali date": jdate[:16]})

    def gold_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: iran_local.
        iran_local = db.iran_local
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting 18-Karat Gold Price, Current time and Run Count.
        price = iran_local.insert_one({"name": "18 Karat Gold", "price": self.gold_price + ' Rials',
                                       "Run Count": self.run_count_gold, "date": date[:16], "jalali date": jdate[:16]})

    def gold_coin_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: iran_local.
        iran_local = db.iran_local
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting Gold Coin Price, Current time and Run Count.
        price = iran_local.insert_one({"name": "Gold Coin", "price": self.gold_coin_price + ' Rials', "Run Count":
                                       self.run_count_gold_coin, "date": date[:16], "jalali date": jdate[:16]})

    def dollar_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: iran_local.
        iran_local = db.iran_local
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting US Dollar Price, Current time and Run Count.
        price = iran_local.insert_one({"name": "US Dollar", "price": self.dollar_price + ' Rials', "Run Count":
                                       self.run_count_dollar, "date": date[:16], "jalali date": jdate[:16]})

    def stock_market_mongo_db(self):
        # Connecting to DataBase.
        mongo_client = MongoClient("localhost", 27017)
        # DataBase Name: market.
        db = mongo_client.market
        # Collection Name: iran_local.
        iran_local = db.iran_local
        # Getting current time (momentary year, month, day, etc).
        current_time = datetime.datetime.now()
        current_jalali_time = jdatetime.datetime.now()
        date = str(current_time)
        jdate = str(current_jalali_time)
        # Inserting Total Index of Iran Stock Exchange amount, Current time and Run Count.
        price = iran_local.insert_one({"name": "Total Index of Iran Stock Exchange", "amount": self.stock_market_amount
                                      + ' Million', "Run Count": self.run_count_stock_market, "date": date[:16],
                                       "jalali date": jdate[:16]})
