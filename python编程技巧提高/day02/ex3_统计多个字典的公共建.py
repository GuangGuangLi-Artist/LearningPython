#coding=utf-8
from random import randint,sample

def some_dict_count():
    data1 = {x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
    data2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    data3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    res = []
    for k in data1:
        if k in data2 and k in data3:
            res.append(k)
    return res
if __name__ == '__main__':
    sdc = some_dict_count()
    print(sdc)
