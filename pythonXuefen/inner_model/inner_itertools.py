#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
'''
import itertools
import os



def write_it():
    it_count = itertools.count(1,3) #0开始 步长为3的迭代器
    file_path = os.getcwd() + '\\inner_model\\for_it'
    with open(file=file_path,mode='w') as f:
        list_a = []
        for i in it_count:
            if i == 161509:
                break
            list_a.append(i)
        f.write(str(list_a))

def it_cycle():
    it_c = itertools.cycle('ABC')#无限重复下去
    for s in it_c:
        print(s)

def it_repeat():
    it_p = itertools.repeat('ABC',3)#重复3次
    for s in it_p:
        print(s)

def it_chain():
    it_p = itertools.chain('ABC','XYZ')#拼接
    for s in it_p:
        print(s)

def it_groupby():
    it_g = itertools.groupby('ABCSGSGGSGSABBBACBCBCBCBYDTDSGSGGSGSABBBACBCBCBCBYDTD',lambda c:c.upper())#拼接
    for key,group in it_g:
        print(key,list(group))

if __name__ == '__main__':
    #write_it()
    #it_cycle()
    #it_repeat()
    #it_chain()
    it_groupby()




