#coding=utf-8


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import string

def run():
    df = pd.read_csv("./file/IMDB-Movie-Data.csv")

    #统计分类的列表
    temp_list = df["Genre"].str.split(",").tolist()
    genre_list = list(set(i for j in temp_list for i in j))

    #构造全为0的数组
    zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
    # print(zeros_df)


    #给每个电影出现分类的位置赋值
    for i in range(df.shape[0]):
        zeros_df.loc[i,temp_list[i]] = 1

    # print(zeros_df.head(3))

    #统计每个分类的电影的数量的和

    genre_count = zeros_df.sum(axis=0)
    # print(genre_count)

    #paixu
    genre_count = genre_count.sort_values()
    _x = genre_count.index
    _y = genre_count.values


    #画图
    plt.figure(figsize=(16,10),dpi=100)
    plt.bar(range(len(_x)),_y)
    plt.xticks(range(len(_x)),_x)
    plt.show()

if __name__ == '__main__':
    run()