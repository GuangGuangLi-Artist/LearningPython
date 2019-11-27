#coding=utf-8

import threading

def deadLoop():
    while True:
        pass

def main():
    t = threading.Thread(target=deadLoop)
    t.start()

    deadLoop()

if __name__ == "__main__":
    main()