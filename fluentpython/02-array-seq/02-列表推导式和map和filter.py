#coding=utf-8


#列表推导式
symbols = "$¥€£¤￠"
beyond_ascii = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond_ascii)
print("*" * 50)

#map和filter

beyond_ascii_1 = list(filter(lambda c: c>127,map(ord,symbols)))
print(beyond_ascii_1)