#coding=utf-8

from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        pass

classmate = Classmate()

classmate.add("李广")
classmate.add("苏彪")
classmate.add("陈诚")

print("判断classmate是否是可以迭代的对象",isinstance(classmate,Iterable))


for name in classmate:
    print(name)