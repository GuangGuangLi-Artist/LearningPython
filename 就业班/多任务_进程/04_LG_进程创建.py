#coding=utf-8


import multiprocessing
import time

def test():
    """子进程要执行的代码"""
    while True:
        print("这是子进程2---")
        time.sleep(2)


def main():
    p = multiprocessing.Process(target=test)
    p.start()
    while True:
        print("这是主进程1---")
        time.sleep(2)



if __name__ == "__main__":
    main()