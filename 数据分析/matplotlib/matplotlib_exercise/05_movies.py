#coding=utf-8

from matplotlib import pyplot as plt
import matplotlib
import random

def movies():
    font = {'family' : 'MicroSoft YaHei',
            'weight' : 'bold'
            }
    matplotlib.rc("font",**font)

    a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：\n最后的骑士","摔跤吧！爸爸","加勒比海盗5：\n死无对证","金刚：骷髅岛","极限特工：\n终极回归","生化危机6：\n终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
    b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23] 


    plt.figure(figsize=(24,15),dpi=100)

    #绘制条形图
    # plt.bar(range(len(a)),b,width=0.3)

    #绘制横着的直方图
    plt.barh(range(len(a)),b,height=0.3,color="cyan")
      
    
    #这是竖着的图对应的轴
    # plt.xticks((range(len(a)),a,rotation=45)
    
    #这是横着的图对应的轴
    plt.yticks(range(len(a)),a)

    plt.xlabel("票房")
    plt.ylabel("电影名")
    plt.grid(alpha=0.3)
    plt.show()

if __name__ == "__main__":
    movies()