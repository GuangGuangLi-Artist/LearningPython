#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
内建模块
    datetime
    collections
        namedtuple
        deque
        defaultdict
        OrderedDict
        ChainMap 可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dic 即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。
        Counter Counter是一个简单的计数器，例如，统计字符出现的个数
    
'''
import datetime
import collections
import argparse
import os
dt = datetime.datetime(2025,5,26,18,20)
dt_timestamp = dt.timestamp() #timestamp
print(dt)
print(dt_timestamp)
print(datetime.datetime.fromtimestamp(1748254800.0))#timestamp转化为datetime
#str转化为datatime
cday = datetime.datetime.strptime('2025-05-26 21:02:22','%Y-%m-%d %H:%M:%S')
print(cday)
#datatime转化为str
now = datetime.datetime.now()
print(now)
print(now.strftime('%a,%b %d %H:%M'))

#datetime加减 timedelta
oneday_after = now + datetime.timedelta(days=1)
print(oneday_after)

#namedtuple是一个函数，它用来创建一个自定义的tuple对象
point = collections.namedtuple('Point',['x','y'])
p = point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,point))
print(isinstance(p,tuple))

deq = collections.deque(['a','b','c'])
deq.append('x')
deq.appendleft('y')
print(deq)
print('---------------------')
dd = collections.defaultdict(lambda:'N/A')
dd['key1'] = 'a'
print(dd['key1'])  
print(dd['key2'])
print('---------------------')
do = collections.OrderedDict([('a',1),('c',3),('b',2)]) #按照插入顺序排序
print(do)
for k,v in do.items():
    print(k,':', v)

print('---------------------')

#默认参数
defaults = {
    'color':'red',
    'user':'guest'
}

#命令行参数
parse = argparse.ArgumentParser()
parse.add_argument('-u','--user')
parse.add_argument('-c','--color')
namespace = parse.parse_args()
command_line_args = {k:v for k,v in vars(namespace).items() if v}

#组合成chainMap
combined = collections.ChainMap(command_line_args,os.environ,defaults)

#打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
print('---------------------')
co = collections.Counter('hello')
print(co)
co.update('lig') #原字符串基础上添加字符串之后统计字符出现个数
print(co)
print('---------------------')

