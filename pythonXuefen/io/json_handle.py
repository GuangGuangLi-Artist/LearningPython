#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle
import os
import json

'''
序列化
    把变量从内存中变成可存储或传输的过程称之为序列化
    Python提供了pickle模块来实现序列化
'''
file_path = os.getcwd() + '\\io\\for_pickle'
def pickle_test():
    d = dict(name='Bob', age=20, score=88)
    bys = pickle.dumps(d)
    with open(file=file_path,mode='bw') as f:
        f.write(bys)
    
    with open(file=file_path,mode='br') as f:
        ds = pickle.load(f)
        print(ds)



class Student_js():
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score,
    }

def dict2student(std):
    return Student_js(std['name'],std['age'],std['score'])

if __name__ == '__main__':
    #pickle_test()
    sj = Student_js('Bob', 20, 88)
    print(json.dumps(sj,default=student2dict))
    print(json.dumps(sj,default=lambda obj:obj.__dict__))
    js_str = '{"name": "Alice", "age": 22, "score": 68}'
    st = json.loads(js_str,object_hook=dict2student)
    print(st.name)
    print(st.age)
    print(st.score)



