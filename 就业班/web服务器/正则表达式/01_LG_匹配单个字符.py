#coding=utf-8

import re

ret1 = re.match("哈利波特\d","哈利波特8,哈利波特9")
ret2 = re.match("哈利波特[1-8]","哈利波特4")
ret3 = re.match("哈利波特[1234789]","哈利波特7")
ret4 = re.match("哈利波特[1234789]","哈利波特6")
ret5 = re.match("哈利波特.","哈利波特m")

print(ret1.group())
print(ret2.group())
print(ret3.group())
#print(ret4.group())  AttributeError: 'NoneType' object has no attribute 'group'
print(ret5.group())

http://python.usyiyi.cn/translate/python_352/index.html