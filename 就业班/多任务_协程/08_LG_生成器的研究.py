#coding=utf-8

def fib(all_num):

    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        #print(a)
        yield a #如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num +=1
    return "---ok---"#如果想要获取这个返回值，则在生成器结束时的异常对象属性里获取这个值

#如果在调用fib()函数的时候，发现这个函数中有yield,不是调用函数，而是创建一个生成器对象
obj = fib(20)


# ret1 = next(obj)
# print(ret1)
#
# ret2 = next(obj)
# print(ret2)

'''
  File "E:/pythonWorkspace/LearningPython/就业班/多任务_协程/08_LG_生成器的研究.py", line 23, in <module>
    ret2 = next(obj)
StopIteration
'''
# ret2 = next(obj)
# print(ret2)

while True:
    try:
        ret = next(obj)
        print(ret)
    except Exception as f:
        value_ok = f.value
        print(value_ok)
        break


