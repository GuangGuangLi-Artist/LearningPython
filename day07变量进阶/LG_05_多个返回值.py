#coding=utf-8

def measure():
    """测量温度和湿度"""
    print("测量开始")
    temp = "39"
    wetness = "50"
    print("测量结束")


    #远足-可以包含多个数据，可以使用元组让函数返回多个值
    return "temp:" + temp,"wetness:" + wetness

result = measure()
print(result)


#需要单独处理温度或者湿度
print(result[0])
print(result[1])
print("===================================")

#如果函数的返回类型是元组，同时希望单独的处理元组中的元素，可以使用
#多个变量，一次接收函数的返回结果

gl_temp,gl_wetness = measure()
print(gl_temp)
print(gl_wetness)