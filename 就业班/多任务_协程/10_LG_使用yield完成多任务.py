#coding=utf-8


import time

def test1():
    while True:
        print("---1---")
        time.sleep(0.1)
        yield



def test2():
    while True:
        print("---2---")
        time.sleep(0.1)
        yield


def main():
    task_1 = test1()
    task_2 = test2()
    while True:
        next(task_1)
        next(task_2)


if __name__ == "__main__":
    main()