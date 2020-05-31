#coding=utf-8

from collections import OrderedDict


def dict_youxu():
    d = OrderedDict()
    d['li'] = (1,35)
    d['leo'] = [2,37]
    d['ami'] = [3,40]
    for k in d:
        print(k,d[k])


if __name__ == '__main__':
    dict_youxu()