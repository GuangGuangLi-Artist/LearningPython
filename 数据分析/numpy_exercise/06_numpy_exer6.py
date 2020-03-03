#coding=utf-8

import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def run():
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

    t_us = np.loadtxt(us_file_path,delimiter=",",dtype=int)

    t_us_comments = t_us[:,-1]

    t_us_comments = t_us_comments[t_us_comments<=5000]
    d = 250
    bin_nums = (t_us_comments.max()-t_us_comments.min())//d

    plt.figure(figsize=(16,10),dpi=100)
    plt.hist(t_us_comments,bin_nums)
    plt.show()

if __name__ == '__main__':
    run()