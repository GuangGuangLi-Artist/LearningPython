#coding=utf-8


import re

ret1 = re.match(r"哈利波特\d{1,3}","哈利波特123")
ret2 = re.match(r"\d{11}","12345678901")
ret3 = re.match("021-?\d{8}","021-12345678")
ret4 = re.match("021-?\d{8}","021123456787")
ret5 = re.match(r"\d{3,4}-?\d{7,8}","0532-12345678")
html_content = """hksahdfkjashkdfhsakj
jfsljfdlsaj
jfaslkjflkdas
ajsflkdsajfl"""
ret6 = re.match(r".*",html_content)
ret7 = re.match(r".*",html_content,re.S)
ret8 = re.match(r".*","")
ret9 = re.match(r".+","")




print(ret1.group())
print(ret2.group())
print(ret3.group())
print(ret4.group())
print(ret5.group())
print(ret6.group())
print("-"*50)
print(ret7.group())
print(ret8.group())
#print(ret9.group())