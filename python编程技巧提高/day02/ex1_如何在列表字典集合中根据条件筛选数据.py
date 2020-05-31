#coding=utf-8

from random import randint

def guolv():
    '''迭代方法实现列表中负数的筛选'''
    data = [3,9,-1,10,20,-9,32,0,-3]
    data_res = []
    for i in data:
        if i > 0:
            data_res.append(i)
    return data_res


def filter_guolv():
    '''filter函数过滤获取过滤数据'''
    data = [randint(-10,10) for x in range(10)]
    data_filter = filter(lambda x: x >= 0,data)
    data_res = []

    for i in data_filter:
        data_res.append(i)
    return data_res

def liebiaojiexi_guolv():
    '''列表解析过滤数据'''
    data = [randint(-10,10) for i in range(10)]
    res = [x for x in data if x>=0]
    return res

def dict_guolv():
    '''字典的过滤'''
    dict_data = {x:randint(60,100) for x in range(21)}
    res = {k:v for k,v in dict_data.items()if v > 90}
    return res

def set_guolv():
    '''集合的过滤'''
    data = set(randint(-10,10) for x in range(10))
    res = {x for x in data if x % 3 == 0}
    return res
if __name__ == '__main__':
   # dr = filter_guolv()
   # print(dr)

   # lbjx_res = liebiaojiexi_guolv()
   # print(lbjx_res)

   # di_gv = dict_guolv()
   # print(di_gv)

   set_gv = set_guolv()
   print(set_gv)



