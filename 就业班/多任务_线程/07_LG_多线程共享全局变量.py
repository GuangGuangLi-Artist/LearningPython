#coding=utf-8

import threading
import time


#定义全局变量
num = 100

def test1():
    global num
    num += 100
    print("---in test1---%d" % num)

def test2():
    print("---in test2---%d" % num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()

    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main thread --%d " % num)





if __name__ == "__main__":
    main()