#coding=utf-8
import multiprocessing
import os
import time


num = [11,22]

def work1():
    """子进程要执行的代码"""
    print("in process1 pid=%d,num=%s" %(os.getpid(), num))
    for i in range(10):
        num.append(i)
        time.sleep(1)
        print("in process1 pid=%d,num=%s" % (os.getpid(),num))

def work2():
    print("in process2 pid=%d,num=%s" % (os.getpid(),num))


def main():
    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)

    p1.start()
    p1.join()

    p2.start()


if __name__ == "__main__":
    main()