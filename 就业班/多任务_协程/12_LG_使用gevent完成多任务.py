#coding=utf-8


import gevent
import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(1)
        gevent.sleep(1)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(1)
        gevent.sleep(1)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(1)
        gevent.sleep(1)

print("---1---")
g1 = gevent.spawn(f1,5)
print("---2---")
g2 = gevent.spawn(f2,6)
print("---3---")
g3 = gevent.spawn(f3,7)
print("---4---")

g1.join()
g2.join()
g3.join()
