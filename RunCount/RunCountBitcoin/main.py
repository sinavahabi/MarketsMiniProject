def bitcoin_run_count():
    if True:
        # Open file in read mode.
        count_file_btc = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                              "RunCount/RunCountBitcoin/bitcoin_count.txt", "r")
        # Read data.
        count = count_file_btc.read()
        # Close data.
        count_file_btc.close()

        # Open file again but in write mode.
        count_file_btc = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                              "RunCount/RunCountBitcoin/bitcoin_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_btc.write(str(count))
        # Close file.
        count_file_btc.close()

    return count
