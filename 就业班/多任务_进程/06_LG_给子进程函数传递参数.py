#coding=utf-8

import multiprocessing
import time
import os

def test(name,age,**kwargs):
   for i in range(10):
       print('子进程运行中，name= %s,age=%d,pid=%d...' % (name, age, os.getpid()))
       print(kwargs)
       time.sleep(0.2)

def main():
    p = multiprocessing.Process(target=test, args=('test', 18), kwargs={"m": 20})
    p.start()
    time.sleep(1)
    p.terminate()
    p.join()


if __name__ == "__main__":
    main()


