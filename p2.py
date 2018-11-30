import pandas as pd

def corruption_checksum(df):
    checksum = 0
    for index, row in df.iterrows():
        max = row.max()
        min = row.min()
        checksum += max - min
        print("max:{}, min:{}, checksum:{}".format(max,min,checksum))

    return checksum
