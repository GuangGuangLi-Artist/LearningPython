#coding=utf-8
import multiprocessing
import time
import os


def test():
    """子进程要执行的代码"""
    print('子进程运行中 pid=%d' % (os.getpid()))
    print("子进程运行结束")

def main():
    print('父进程运行中 pid=%d' % (os.getpid()))
    p = multiprocessing.Process(target=test)
    p.start()

if __name__ == '__main__':
    main()