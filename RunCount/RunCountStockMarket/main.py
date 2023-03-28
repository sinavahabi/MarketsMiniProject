def stock_market_run_count():
    if True:
        # Open file in read mode.
        count_file_stock_market = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                       "RunCount/RunCountStockMarket/stock_market_count.txt", "r")
        # Read data.
        count = count_file_stock_market.read()
        # Close data.
        count_file_stock_market.close()

        # Open file again but in write mode.
        count_file_stock_market = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                       "RunCount/RunCountStockMarket/stock_market_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_stock_market.write(str(count))
        # Close file.
        count_file_stock_market.close()

    return count
