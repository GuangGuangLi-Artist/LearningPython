#coding=utf-8

import numpy as np

def run():

    us_data = "./youtube_video_data/US_video_data_numbers.csv"
    uk_data = "./youtube_video_data/GB_video_data_numbers.csv"

    us_data = np.loadtxt(us_data,delimiter=",",dtype=int)
    uk_data = np.loadtxt(uk_data,delimiter=",",dtype=int)

    zeros_data = np.zeros((us_data.shape[0],1)).astype(int)
    ones_data = np.ones((uk_data.shape[0],1)).astype(int)

    us_data = np.hstack((us_data,zeros_data))
    uk_data = np.hstack((uk_data,ones_data))

    final_data = np.vstack((us_data,uk_data))
    print(final_data)

if __name__ == '__main__':
    run()