"""
    This is updated version of 'Market Status' program, and it was writen in OOP method.
"""

# Installing essential libraries and packages which can be run in your terminal, virtual env, etc.:
# Commands:
# pip install bs4
# pip install requests

import re
import requests
from bs4 import BeautifulSoup


# After importing all the essential packages that we need, our program is ready to begin.

'''
    By Instantiating API class at first stage we get and read desired data (Bitcoin price for example) from web. 
    Each method has been defined to get a specific data from web (Ethereum Price, Gold Coin Price and etc).
    By using regex we remove every unessential other stuff that we get from web by the way. 
'''


# Instantiating API class.
class API:
    def __init__(self):
        self.btc_link = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
        self.eth_link = 'https://coinmarketcap.com/currencies/ethereum/'
        self.bnb_link = 'https://coinmarketcap.com/currencies/bnb/'
        self.gold_link = 'https://www.tgju.org/profile/geram18'
        self.gold_coin_link = 'https://www.tgju.org/profile/sekee'
        self.dollar_link = 'https://www.tgju.org/profile/crypto-tether'
        self.stock_market_link = 'https://www.shakhesban.com/markets/index/%D8%B4-%DA%A9%D9%84-%D8%A8%D9%88%D8%B1%D8%B3'
        self.final_result_btc, self.final_result_eth, self.final_result_bnb = '', '', ''
        self.final_result_gold, self.final_result_gold_coin, self.final_result_dollar, self.final_result_market = '', '','', ''
        self.btc_price, self.eth_price, self.bnb_price = '', '', ''
        self.gold_price, self.gold_coin_price, self.dollar_price, self.stock_market_amount = '', '', '', ''

    def btc_api(self):
        # Bitcoin API.
        response_btc = requests.get(self.btc_link)
        res_btc = response_btc.text
        soup = BeautifulSoup(res_btc, "html.parser")
        result_btc = soup.find('div', attrs={'class': 'priceValue'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_btc = result_btc.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')

        self.btc_price = re.sub(r'\$', '', self.final_result_btc)
        return self.btc_price

    def eth_api(self):
        # Ethereum API.
        response_eth = requests.get(self.eth_link)
        res_eth = response_eth.text
        soup = BeautifulSoup(res_eth, "html.parser")
        result_eth = soup.find('div', attrs={'class': 'priceValue'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_eth = result_eth.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')
        self.eth_price = re.sub(r'\$', '', self.final_result_eth)
        return self.eth_price

    def bnb_api(self):
        # BNB API.
        response_bnb = requests.get(self.bnb_link)
        res_bnb = response_bnb.text
        soup = BeautifulSoup(res_bnb, "html.parser")
        result_bnb = soup.find('div', attrs={'class': 'priceValue'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_bnb = result_bnb.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')
        self.bnb_price = re.sub(r'\$', '', self.final_result_bnb)
        return self.bnb_price

    def gold_api(self):
        # 18 Karat Gold API.
        response_gold = requests.get(self.gold_link)
        res_gold = response_gold.text
        soup = BeautifulSoup(res_gold, "html.parser")
        result_gold = soup.find('td', attrs={'class': 'text-left'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_gold = result_gold.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')

        self.gold_price = re.sub(r'[^,\d]', '', self.final_result_gold)
        return self.gold_price

    def gold_coin_api(self):
        # Gold Coin API.
        response_gold_coin = requests.get(self.gold_coin_link)
        res_gold_coin = response_gold_coin.text
        soup = BeautifulSoup(res_gold_coin, "html.parser")
        result_gold_coin = soup.find('td', attrs={'class': 'text-left'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_gold_coin = result_gold_coin.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')

        self.gold_coin_price = re.sub(r'[^,\d]', '', self.final_result_gold_coin)
        return self.gold_coin_price

    def dollar_api(self):
        # US Dollar API.
        response_dollar = requests.get(self.dollar_link)
        res_dollar = response_dollar.text
        soup = BeautifulSoup(res_dollar, "html.parser")
        result_dollar = soup.find_all('td', attrs={'class': 'text-left'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_dollar = result_dollar[1].text
        except AttributeError and IndexError as attr_error:
            print('Oops! something wen\'t wrong!')

        self.dollar_price = re.sub(r'[^,\d]', '', self.final_result_dollar)
        return self.dollar_price

    def stock_market_api(self):
        # Total Index of Iran Stock Exchange API.
        response_stock_market = requests.get(self.stock_market_link)
        res_stock_market = response_stock_market.text
        soup = BeautifulSoup(res_stock_market, "html.parser")
        result_stock_market = soup.find('span', attrs={'dir': 'ltr'})
        # Avoiding program crashes for website bad responses sometimes, issues etc.
        try:
            self.final_result_market = result_stock_market.text
        except AttributeError as attr_error:
            print('Oops! something wen\'t wrong!')

        self.stock_market_amount = re.sub(r'[^0-9.]', '', self.final_result_market)
        return self.stock_market_amount
