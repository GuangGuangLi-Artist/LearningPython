#coding=utf-8



import numpy as np


def run():
    '''
    [1 2 3]
<class 'numpy.ndarray'>
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
[4 6 8]
<class 'numpy.ndarray'>
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


if __name__ == '__main__':
    run()