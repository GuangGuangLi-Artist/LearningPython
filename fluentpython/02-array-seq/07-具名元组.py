#coding=utf-8

#定义和使用具名元组
from collections import namedtuple

city = namedtuple('City','name country population coordianates')
tokyo = city('toyko','jp',26.933,(35.689722,139.691667))
print(tokyo)
print(tokyo.population)