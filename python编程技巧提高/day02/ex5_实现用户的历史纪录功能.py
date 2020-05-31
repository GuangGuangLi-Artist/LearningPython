#coding=utf-8

from collections import deque
from random import randint
import pickle

N = randint(0,101)
history = deque([],5)

def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less than N' % k)
    else:
        print("%s is greter than N" % k)
    return False

while True:
    data = input("请猜一个100内的数字: ")
    if data.isdigit():
        k = int(data)
        history.append(k)
        if guess(k):
            break

    elif data == 'history' or data == 'h?':
        print(list(history))

