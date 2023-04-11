"""
    By Instantiating Counter class in second stage we count every single time that program has been running and
    data has been returned to database.
    Each method has been defined to count a specific element which has been inserted to database everytime program
    has been running. For example each time we get Bitcoin price data from web in APi class the count object
    (count txt file) is added by one.
"""


# Instantiating Counter class.
class Counter:
    def __init__(self):
        self.run_count_btc, self.run_count_eth, self.run_count_bnb = 0, 0, 0
        self.run_count_gold, self.run_count_gold_coin, self.run_count_dollar, self.run_count_stock_market = 0, 0, 0, 0

    # Bitcoin Counter.
    def bitcoin_run_count(self):
        if True:
            # Open file in read mode.
            count_file_btc = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                  "RunCountBitcoin/bitcoin_count.txt", "r")
            # Read data.
            count = count_file_btc.read()
            # Close data.
            count_file_btc.close()

            # Open file again but in write mode.
            count_file_btc = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                  "RunCountBitcoin/bitcoin_count.txt", "w")
            # Increase the count value by adding 1.
            count = int(count) + 1
            # write count to file.
            count_file_btc.write(str(count))
            # Close file.
            count_file_btc.close()

        return count

    def bitcoin_run_count_reader(self):
        # By reading count from txt file we can insert it to DataBase.
        btc_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountBitcoin/"
                        "bitcoin_count.txt", 'r')
        self.run_count_btc = btc_file.read()
        return self.run_count_btc

# Now we repeat same structure for other methods.
    # Ethereum Counter.
    def ethereum_run_count(self):
        if True:
            count_file_eth = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                  "RunCountEthereum/ethereum_count.txt", "r")
            count = count_file_eth.read()
            count_file_eth.close()
            count_file_eth = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                  "RunCountEthereum/ethereum_count.txt", "w")
            count = int(count) + 1
            count_file_eth.write(str(count))
            count_file_eth.close()

        return count

    def ethereum_run_count_reader(self):
        eth_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountEthereum/"
                        "ethereum_count.txt", 'r')
        self.run_count_eth = eth_file.read()

    # BNB Counter.
    def bnb_run_count(self):
        if True:
            count_file_bnb = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountBNB/"
                                  "bnb_count.txt", "r")
            count = count_file_bnb.read()
            count_file_bnb.close()
            count_file_bnb = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountBNB/"
                                  "bnb_count.txt", "w")
            count = int(count) + 1
            count_file_bnb.write(str(count))
            count_file_bnb.close()

        return count

    def bnb_run_count_reader(self):
        bnb_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountBNB/"
                        "bnb_count.txt", 'r')
        self.run_count_bnb = bnb_file.read()

    # Gold Counter.
    def gold_run_count(self):
        if True:
            count_file_gold = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountGold/"
                                   "gold_count.txt", "r")
            count = count_file_gold.read()
            count_file_gold.close()
            count_file_gold = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountGold/"
                                   "gold_count.txt", "w")
            count = int(count) + 1
            count_file_gold.write(str(count))
            count_file_gold.close()

        return count

    def gold_run_count_reader(self):
        gold_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountGold/"
                         "gold_count.txt", 'r')
        self.run_count_gold = gold_file.read()

    # Gold Coin Counter.
    def gold_coin_run_count(self):
        if True:
            count_file_gold_coin = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                        "RunCountGoldCoin/gold_coin_count.txt", "r")
            count = count_file_gold_coin.read()
            count_file_gold_coin.close()
            count_file_gold_coin = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                        "RunCountGoldCoin/gold_coin_count.txt", "w")
            count = int(count) + 1
            count_file_gold_coin.write(str(count))
            count_file_gold_coin.close()

        return count

    def gold_coin_run_count_reader(self):
        gold_coin_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountGoldCoin/"
                              "gold_coin_count.txt", 'r')
        self.run_count_gold_coin = gold_coin_file.read()

    # Dollar Counter.
    def dollar_run_count(self):
        if True:
            count_file_dollar = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                     "RunCountDollar/dollar_count.txt", "r")
            count = count_file_dollar.read()
            count_file_dollar.close()
            count_file_dollar = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/"
                                     "RunCount/RunCountDollar/dollar_count.txt", "w")
            count = int(count) + 1
            count_file_dollar.write(str(count))
            count_file_dollar.close()

        return count

    def dollar_run_count_reader(self):
        dollar_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/RunCountDollar/"
                           "dollar_count.txt", 'r')
        self.run_count_dollar = dollar_file.read()

    # Stock Market Counter.
    def stock_market_run_count(self):
        if True:
            count_file_stock_market = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                           "RunCountStockMarket/stock_market_count.txt", "r")
            count = count_file_stock_market.read()
            count_file_stock_market.close()
            count_file_stock_market = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                           "RunCountStockMarket/stock_market_count.txt", "w")
            count = int(count) + 1
            count_file_stock_market.write(str(count))
            count_file_stock_market.close()

        return count

    def stock_market_run_count_reader(self):
        stock_market_file = open("C:/Users/Asus/Desktop/My Projects/Python/MarketsMiniProject/RunCount/"
                                 "RunCountStockMarket/stock_market_count.txt", 'r')
        self.run_count_stock_market = stock_market_file.read()
