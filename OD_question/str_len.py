# coding=utf-8


import sys

def last_len():
    a = []
    for line in sys.stdin:
        a = line.split(' ')
        last_word = a[-1]
        print(len(last_word))



if __name__ == '__main__':
    last_len()
