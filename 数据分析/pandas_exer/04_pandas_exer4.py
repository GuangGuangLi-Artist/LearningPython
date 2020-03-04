#coding=utf-8


import pandas as pd
import numpy as np
import string

def run():
    df = pd.read_csv("./file/dogNames2.csv")
    #排序
    df = df.sort_values(by="Count_AnimalName",ascending=False)
    print(df.head(5))

    print(df[:20])
    print("*"* 20)
    print(df[:20]["Row_Labels"])
    print("*" * 20)
    print(df[(df["Row_Labels"].str.len()>4)&(df["Count_AnimalName"]>700)])


if __name__ == '__main__':
    run()