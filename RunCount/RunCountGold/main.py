def gold_run_count():
    if True:
        # Open file in read mode.
        count_file_gold = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                               "RunCount/RunCountGold/gold_count.txt", "r")
        # Read data.
        count = count_file_gold.read()
        # Close data.
        count_file_gold.close()

        # Open file again but in write mode.
        count_file_gold = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                               "RunCount/RunCountGold/gold_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_gold.write(str(count))
        # Close file.
        count_file_gold.close()

    return count
