def dollar_run_count():
    if True:
        # Open file in read mode.
        count_file_dollar = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                 "RunCount/RunCountDollar/dollar_count.txt", "r")
        # Read data.
        count = count_file_dollar.read()
        # Close data.
        count_file_dollar.close()

        # Open file again but in write mode.
        count_file_dollar = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                                 "RunCount/RunCountDollar/dollar_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_dollar.write(str(count))
        # Close file.
        count_file_dollar.close()

    return count
