def ethereum_run_count():
    if True:
        # Open file in read mode.
        count_file_eth = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                              "RunCount/RunCountEthereum/ethereum_count.txt", "r")
        # Read data.
        count = count_file_eth.read()
        # Close data.
        count_file_eth.close()

        # Open file again but in write mode.
        count_file_eth = open("F:/Workspace/PycharmProjects/MarketsMiniProject/"
                              "RunCount/RunCountEthereum/ethereum_count.txt", "w")
        # Increase the count value by adding 1.
        count = int(count) + 1
        # write count to file.
        count_file_eth.write(str(count))
        # Close file.
        count_file_eth.close()

    return count
