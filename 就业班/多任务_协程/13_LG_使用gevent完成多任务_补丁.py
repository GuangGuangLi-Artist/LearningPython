#coding=utf-8


import gevent
import time
from gevent import monkey


#有耗时操作时需要
monkey.patch_all()

def f1(n):
    for i in range(10):
        print(n,i)
        time.sleep(1)
        #gevent.sleep(1)

# print("---1---")
# g1 = gevent.spawn(f1,5)
# print("---2---")
# g2 = gevent.spawn(f2,6)
# print("---3---")
# g3 = gevent.spawn(f3,7)
# print("---4---")

# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(f1,"work1"),
    gevent.spawn(f1,"work2")

])
