#coding=utf-8

import numpy as np
import random


def run():
    t1 = np.arange(12)
    t2 = t1.reshape((3,4))
    print(t2)
    print("--" * 10)
    '''
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
    
    '''

    t3 = np.arange(24)
    t4 = t3.reshape((2,3,4))
    print(t4)
    print("--" * 10)
    '''
    [[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
  '''

    t5 = t4.reshape((4,6))
    print(t5)
    print(type(t5))
    print("--" * 10)

    '''
    t6和t7,t8的区别，t7是一个二维的数组
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
--------------------
[[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]]
--------------------
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
'''
    t6 = t5.reshape((24,))
    print(t6)
    print("--" * 10)
    t7 = t5.reshape(1,24)
    print(t7)
    print("--" * 10)

    t8 = t5.flatten()
    print(t8)
    print("--" * 10)

    t9 = t5 + 2
    print(t9)
    print("--" * 10)

    t0 = np.arange(100,124).reshape((4,6))
    t11 = t5 + t0
    print(t11)
    print("--" * 10)

    '''
    [[ 0  0  0  0  0  0]
 [ 6  6  6  6  6  6]
 [12 12 12 12 12 12]
 [18 18 18 18 18 18]]
 '''
    t12 = np.arange(0,6)
    t13 = t5 - t12
    print(t13)
    print("--" * 10)

    '''

    '''
    t14 = np.arange(4).reshape((4,1))
    t15 = t5 - t14
    print(t15)
    print("--" * 10)








if __name__ == "__main__":
    run()