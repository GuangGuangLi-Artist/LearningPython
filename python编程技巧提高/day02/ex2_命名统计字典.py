#coding=utf-8
from collections import  namedtuple,Counter
from random import randint
import re


def tuple_named():
    '''命名'''
    Student = namedtuple('Student',['name','age','male','email'])
    s = Student('subiao','20','女','123@qq.com')
    return s

def dict_count():
    '''统计'''
    data = [randint(-10,10) for x in range(30)]
    c_data = dict.fromkeys(data,0)
    for i in data:
        c_data[i] += 1
    return c_data

def dict_count_most():
    '''使用Counter进行统计'''
    data = [randint(1,21) for x in range(30)]
    data_c = Counter(data)
    print(data_c)
    data_most = data_c.most_common(3)
    return data_most

def count_word():
    '''导入文件'''
    with open('use_file/user_file.txt','r') as f:
        data = f.read()
    data_count = Counter(re.split('\W+',data))
    print(data_count)
    data_count_most = data_count.most_common(10)
    return data_count_most

def dict_sorted():
    '''字典根据键或值排序'''
    data = {x:randint(60,101) for x in 'abcxyz'}
    data_key = data.keys()
    data_value = data.values()
    #方法一：拼接字典的值
    # data_verse = zip(data_value,data_key)

    #方法二：dict.items()
    data_verse = data.items()
    return sorted(data_verse,key=lambda x:x[1])




if __name__ == '__main__':
    # s1 = tuple_named()
    # print(s1)
    # print(s1.name)

    # dic_cot = dict_count()
    # print(dict_count())

    # data_most = dict_count_most()
    # print(data_most)

    # countword = count_word()
    # print(countword)

    dictsorted = dict_sorted()
    print(dictsorted)