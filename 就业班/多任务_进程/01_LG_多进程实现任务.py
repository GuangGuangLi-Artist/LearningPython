#coding=utf-8

import multiprocessing
import time


def test1():
    while True:
        print("---这是test1----")
        time.sleep(1)


def test2():
    while True:
        print("---这是test2---")
        time.sleep(1)


def main():
    m1 = multiprocessing.Process(target=test1)
    m2 = multiprocessing.Process(target=test2)

    m1.start()
    m2.start()

if __name__ == "__main__":
    main()