#coding=utf-8

#列表作为队列使用
from collections import deque

queue = deque(['li', 'zhou', 'zhao'])
queue.append('wang')
print(queue)

queue.popleft()
print(queue)


def fun_a(a):
    return a ** 2
Fib = list(map(lambda a: a ** 2,range(10)))
Fib_fun = list(map(fun_a,range(5)))
Fib_li_td = [x**2 for x in range(10)]
print(Fib)
print(Fib_fun)
print(Fib_li_td)