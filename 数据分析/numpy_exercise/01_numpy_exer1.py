#coding=utf-8



import numpy as np
import random


def run():
    '''
[1 2 3]
<class 'numpy.ndarray'>
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
[4 6 8]
<class 'numpy.ndarray'>
int32
[1. 2. 3.]
float64
[ True False  True False  True]
bool
[1 0 1 0 1]
int8
[0.68421733 0.41412996 0.99569679 0.45561725 0.25386024 0.65341876
 0.84459894 0.7869969  0.43329345 0.94512313]
float64
[0.68 0.41 1.   0.46 0.25 0.65 0.84 0.79 0.43 0.95]
float64
    '''

    t1 = np.array([1,2,3])
    print(t1)
    print(type(t1))


    t2 = np.array(range(10))
    print(t2)
    print(type(t2))

    t3 = np.arange(4,10,2)
    print(t3)
    print(type(t3))
    print(t3.dtype)

    t4 = np.array(range(1,4),dtype=float)
    print(t4)
    print(t4.dtype)


    t5 = np.array([1,0,3,0,5],dtype=bool)
    print(t5)
    print(t5.dtype)


    t6 = t5.astype("int8")
    print(t6)
    print(t6.dtype)

    t7 = np.array([random.random() for i in range(10)])
    print(t7)
    print(t7.dtype)


    t8 = np.round(t7,2)
    print(t8)
    print(t8.dtype)






if __name__ == '__main__':
    run()