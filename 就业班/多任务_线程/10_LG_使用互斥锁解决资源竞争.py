#coding=utf-8

import threading
import time

num = 0
#创建锁
mutex = threading.Lock()

def test1(n):
    global num
    #上锁
    mutex.acquire()
    for i in range(n):
        num += 1
    #解锁
    mutex.release()
    print("--in test1  num=%d---" %num)


def test2(n):
    global num
    #上锁
    mutex.acquire()
    for i in range(n):
        num += 1
    #解锁
    mutex.release()
    print("--in test2  num=%d---" % num)

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(2     )

    print("----in main thread---num = %d" % num)


if __name__ == "__main__":
    main()