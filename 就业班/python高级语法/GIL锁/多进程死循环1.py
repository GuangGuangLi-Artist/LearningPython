#coding=utf-8

import multiprocessing


def deadLoop():
    while True:
        pass


def main():
    p = multiprocessing.Process(target=deadLoop)
    p.start()

    deadLoop()


if __name__ == "__main__":
    main()