#coding=utf-8

from matplotlib import pyplot as plt
import matplotlib
import random

def movies():
    font = {'family' : 'MicroSoft YaHei',
            'weight' : 'bold'
            }
    matplotlib.rc("font",**font)

    a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
    b_16 = [15746,312,4497,319]
    b_15 = [12357,156,2045,168]
    b_14 = [2358,399,2358,362]

    bar_width = 0.2

    x_l4= list(range(len(a)))
    x_15= [i + bar_width for i in x_l4]
    x_16= [i + bar_width*2 for i in x_l4]
 


    plt.figure(figsize=(24,15),dpi=100)

    #绘制条形图
    # plt.bar(range(len(a)),b,width=0.3)

    #绘制横着的直方图
    plt.bar(range(len(a)),b_14,width=bar_width,label="9月14日")
    plt.bar(x_15,b_15,width=bar_width,label="9月15日")
    plt.bar(x_16,b_16,width=bar_width,label="9月16日")
    
    
    #设置x轴的刻度
    plt.xticks(x_15,a)
    plt.legend(loc="upper left")

    plt.show()

if __name__ == "__main__":
    movies()