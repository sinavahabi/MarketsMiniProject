"""
    We only use this module once to make sure that our specific txt file ('bitcoin_count.txt' for instance) exists
    in order to start counting.
"""

start = 0
count_file_stock_market = open('stock_market_count.txt', 'w+')
count_file_stock_market.write(str(start))
