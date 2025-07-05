#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from contextlib import contextmanager,closing
from urllib.request import urlopen
'''
上下文管理器
    实现方式1
        __enter__
        __exit__
    实现方式2
        @contextmanager
        我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现

'''

class Query_inner():
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('begin')
        return self
    
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('error')
        else:
            print('End')
        
    
    def query(self):
        print('Query info about %s' % self.name)

class Query_contextManager():
    def __init__(self,name):
        self.name = name
        
    def query(self):
        print('Query info about %s' % self.name)
@contextmanager
def create_query(name):
    print('Begin')
    qc = Query_contextManager(name)
    yield qc
    print('End')


'''

    with语句首先执行yield之前的语句，因此打印出<h1>；
    yield调用会执行with语句内部的所有语句，因此打印出hello和world；
    最后执行yield之后的语句，打印出</h1>。

'''
@contextmanager
def create_tag(name):
    print('<%s>' %name)
    yield
    print('<%s>' %name)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

if __name__ == '__main__':
    with Query_inner('bob') as q:
        q.query()
    print('-----------------')
    with create_query('alice') as qc:
        qc.query()
    print('-----------------')

    with create_tag('h1'):
        print('hello')
        print('world')
    print('-----------------')
    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


