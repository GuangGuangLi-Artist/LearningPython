#coding=utf-8
import time


def sing():
    for i in range(5):
        print("___正在唱歌____")
        time.sleep(1)

def dance():
    for i in range(5):
        print("___正在跳舞____")
        time.sleep(1)

def main():
    sing()
    dance()

if __name__ == "__main__":
    main()