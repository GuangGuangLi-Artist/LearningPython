#coding=utf-8

from collections import Iterable
from collections import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想让一个对象成为一个可以迭代的对象，即可以使用for,那么必须实现__iter__方法 """
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num+=1
            return result
        else:
            raise StopIteration

classmate = Classmate()

classmate.add("李广")
classmate.add("苏彪")
classmate.add("陈诚")

#print("判断classmate是否是可以迭代的对象",isinstance(classmate,Iterable))
#classmate_iterator = iter(classmate)
#print("判断classmate_iterator是否是迭代器",isinstance(classmate_iterator,Iterator))


#
for name in classmate:
    print(name)
    time.sleep(1)