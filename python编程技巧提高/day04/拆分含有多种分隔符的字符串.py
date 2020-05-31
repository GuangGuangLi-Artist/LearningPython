#coding=utf-8

import re
def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)),res)
        res = t
    return res

# s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
# res_data = mySplit(s,';,|\t')
# print(res_data)


#使用re模块处理字符串切割

def re_split(s):
    res_s = re.split(r'[;,|\t]+',s)
    print(res_s)
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
res_data = re_split(s)
