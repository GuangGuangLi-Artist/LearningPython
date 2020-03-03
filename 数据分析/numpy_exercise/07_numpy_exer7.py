#coding=utf-8

import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def run():
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

    t_uk = np.loadtxt(uk_file_path,delimiter=",",dtype=int)
    t_uk = t_uk[t_uk[:,1]<=500000]

    t_uk_comment = t_uk[:,-1]
    t_uk_like = t_uk[:,1]


    plt.figure(figsize=(16, 10), dpi=100)
    plt.scatter(t_uk_like, t_uk_comment)
    plt.show()
if __name__ == '__main__':
    run()