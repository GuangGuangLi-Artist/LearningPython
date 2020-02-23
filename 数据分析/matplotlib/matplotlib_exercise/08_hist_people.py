#coding=utf-8

from matplotlib import pyplot as plt
import matplotlib


def hist_people():
    font = {'family' : 'MicroSoft YaHei',
            'weight' : 'bold'
            }
    matplotlib.rc("font",**font)
    plt.figure(figsize=(16,10),dpi=100)

    interval = [0,5,10,15,20,25,30,35,40,45,60,90]
    width = [5,5,5,5,5,5,5,5,5,15,30,60]
    quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

    plt.bar(range(12),quantity,width=1)


    _x = [i - 0.5 for i in range(13)]
    _xtick_labels = interval + [150]

    plt.xticks(_x,_xtick_labels)

    plt.grid()
    plt.show()










if __name__ == "__main__":
    hist_people()