# -*- coding:utf-8 -*- 
import datetime
import functools
'''
装饰器
不修改原函数的基础上给函数添加新功能
装饰器的本质是一个返回函数的高阶函数
'''


#打印日志的装饰器
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper


@log
def now():
    print(datetime.date.today())

now()
print('-----------')

now = log(now)
print(now.__name__)
now()
print('-----------')
#装饰器传入参数
def log_new(text):
    def decorator(func_new):
        def wrapper_new(*args,**kw):
            print('%s %s():' %(text,func_new.__name__))
            return func_new(*args,**kw)
        return wrapper_new
    return decorator



@log_new('execute')
def now_new():
    print(datetime.date.today())

now_new()
print('-----------')
now_new = log_new('execute')(now)
print(now_new.__name__)
now_new()

print('--------')

# 这是标准的不带参数得装饰器

def log_stand(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log_stand
def now_stand():
    print(datetime.date.today())

now_stand()
print('--------')
# 这是标准的带参数得装饰器

def log_stand_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log_stand_param('execute')
def now_stand_param():
    print(datetime.date.today())

now_stand_param()
    

    
   
