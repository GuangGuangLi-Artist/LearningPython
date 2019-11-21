#coding=utf-8


def fib(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>yield>>>",ret)
        a, b = b, a + b
        current_num += 1

obj = fib(10)

#obj.send(None)   send一般不会放到第一次启动生成器时，如果非要这么做，那么传递None

ret = next(obj)
print(ret)

#send里面的数据会传递到第8行，然后ret保存这个结果，send的结果是下一次调用yield时，yield后面的值
ret = obj.send("hello python")
print(ret)