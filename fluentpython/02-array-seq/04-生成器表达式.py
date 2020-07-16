#coding=utf-8
import array

#生成器表达式生成元组
symbols =  "$¥€£¤￠"
tuple_a = tuple(ord(symbol) for symbol in symbols)
#x = ((ord(symbol) for symbol in symbols)
print(tuple_a)

#生成器表达式初始化数组

array_a = array.array('I',(ord(symbol) for symbol in symbols))
print(array_a)


colors = ['balck','white']
sizes = ['S','M','L']
tshirts = ('%s %s' %(c,s) for c in colors for s in sizes)
print(tshirts)
print(type(tshirts))
for tshirt in tshirts:
    print(tshirt)