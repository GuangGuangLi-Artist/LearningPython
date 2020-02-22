#coding=utf-8

import matplotlib
from matplotlib import pyplot as plt 
import random


def make_friens_trends():
    font = {'family' : 'MicroSoft YaHei',
            'weight' : 'bold'
            }
    matplotlib.rc("font",**font)
    x = range(11,31)
    y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
    y_2= [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]


    plt.figure(figsize=(16,10),dpi=100)
    plt.plot(x,y_1,label='自己',color="cyan",linestyle="--",linewidth=2,alpha=0.5)
    plt.plot(x,y_2,label='同桌')


    _xtick_lables = ["{}岁".format(i) for i in x]
    plt.xticks(x,_xtick_lables)
    plt.yticks(range(0,9))
    plt.grid(alpha=0.1)
    
    #添加图例
    plt.legend(loc="upper left")

    plt.ylabel("交友个数")
    plt.xlabel("年龄") 
    plt.title("不同时间的交友个数的统计")


    plt.show()




if __name__ == "__main__":
    make_friens_trends()