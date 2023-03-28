def gold_coin_run_count():
    if True:
        # Open file in read mode.
        count_file_gold_coin = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                    "RunCount/RunCountGoldCoin/gold_coin_count.txt", "r")
        # Read data.
        count = count_file_gold_coin.read()
        # Close data.
        count_file_gold_coin.close()

        # Open file again but in write mode.
        count_file_gold_coin = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                    "RunCount/RunCountGoldCoin/gold_coin_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_gold_coin.write(str(count))
        # Close file.
        count_file_gold_coin.close()

    return count
