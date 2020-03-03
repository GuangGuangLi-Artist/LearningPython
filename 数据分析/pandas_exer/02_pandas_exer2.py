#coding=utf-8


import pandas as pd

def run():
    df = pd.read_csv("./file/dogNames2.csv")
    print(df)


if __name__ == '__main__':
    run()