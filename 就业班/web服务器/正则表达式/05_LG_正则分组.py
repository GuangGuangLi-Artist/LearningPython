#coding=utf-8


import re

ret1 = re.match(r"(^[a-zA-Z0-9_]{4,20})@(163|126)\.com$","laowang@163.com")

html_str = "<body><h1>hahahahah</h1></body>"
ret2 = re.match(r"<(\w*)><(\w*)>.*</\2></\1>",html_str)
ret3 = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>",html_str)

print(ret1.group(1))
print(ret1.group(2))
print(ret2.group())
print(ret3.group())
