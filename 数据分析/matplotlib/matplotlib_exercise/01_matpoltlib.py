#coding=utf-8

from  matplotlib import pyplot as plt
import matplotlib
import random
from matplotlib import font_manager




def main():
    font = {'family' : 'MicroSoft YaHei',
            'weight' : 'bold'
            }
    matplotlib.rc("font",**font)
    matplotlib.rc("font",family="MicroSoft YaHei",weight='bold')
    # my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\Arvo")
    x = range(0,120)
    y = [random.randint(20,35) for i in range(120)]
    plt.figure(figsize=(16,10),dpi=100)
    plt.plot(x,y)

    #调整x轴的刻度
    _x = list(x)
    _xticket_lables = ['10点{}分'.format(i) for i in range(60)]
    _xticket_lables += ['11点{}分'.format(i) for i in range(60)]

    plt.xticks(_x[::3],_xticket_lables[::3],rotation=45)

    #添加描述信息
    plt.xlabel("时间")
    plt.ylabel("温度 单位(℃)")
    plt.title("2小时内的温度变化曲线")

    # plt.xticks(_x[::3],_xticket_lables[::3],rotation=45,fontproperties=my_font)
    plt.show()
    # [20, 21, 22, 22, 31, 33, 26, 22, 23, 35, 22, 22, 23, 21, 34, 23, 24, 26, 29, 26, 20, 27, 33, 31, 22, 35, 31, 24, 31, 21, 31, 23, 32, 28, 26, 22, 29, 31, 32, 30, 23, 34, 25, 22, 25, 27, 34, 28, 34, 23, 33, 31, 21, 30, 22, 28, 35, 31, 33, 31, 25, 29, 34, 29, 20, 32, 20, 27, 35, 22, 23, 35, 35, 31, 31, 27, 27, 24, 21, 31, 31, 34, 25, 27, 29, 21, 22, 27, 23, 23, 23, 31, 25, 27, 28, 28, 31, 23, 30, 34, 22, 25, 23, 22, 35, 22, 27, 26, 32, 22, 28, 24, 31, 22, 24, 31, 35, 25, 35, 21]
    # print(y)
    #120 
    # print(len(y)) 

if __name__ == "__main__":
    main()