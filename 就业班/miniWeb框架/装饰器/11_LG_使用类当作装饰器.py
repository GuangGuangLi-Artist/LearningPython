#coding=utf-8


class Test():

    def __init__(self,para):
        self.para = para


    def __call__(self):
        print("这里是装饰器添加的功能")
        return self.para()



@Test   #get_str=Test(get_str)
def get_str():
    return "我是哈哈"

print(get_str())