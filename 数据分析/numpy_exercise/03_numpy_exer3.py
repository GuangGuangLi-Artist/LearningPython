#coding=utf-8

import numpy as np

def run():
    uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
    us_file_path = "./youtube_video_data/US_video_data_numbers.csv"

    t1 = np.loadtxt(uk_file_path,delimiter=",",dtype="int",unpack=True)
    t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")

    # print(t1)
    # print("*" * 50)
    print(t2)
    print("*" * 50)


    #取行
    print(t2[2])
    print("*" * 50)
    print(t2[2:])

    print("*" * 50)
    #取不连续的多行
    print(t2[[2,8,10]])

    print("*" * 50)

    print("取列了")
    print(t2[:,0])
    print("*" * 50)
    print("*" * 50)
    #取连续的多列
    print(t2[:,2:])
    print("*" * 50)

    #不取连续的多列
    print(t2[:,[0,2]])

    print("取多行多列，取第三行第四列")
    print(t2[2,3])
    print("取多行多列，取第三行到第五行，第二列到第四列")
    print("*" * 50)
    print(t2[2:5,1:4])
    print("*" * 50)
    print("取多个不相领的点")
    print(t2[[0,2,2],[0,1,3]])
    print("修改值")
    t3 = np.arange(24).reshape((4,6))
    print(t3)
    t3[t3<10]=0
    print("*" * 50)
    print(t3)
    print("*" * 50)
    np.where(t3<=15,100,200)
    print(t3)




if __name__ == '__main__':
    run()