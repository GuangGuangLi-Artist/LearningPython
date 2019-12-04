#coding=utf-8

#类方法
class Line(object):

    def __init__(self,k,b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line_5 = Line(1,2)

line_5(1)
line_5(2)
line_5(3)

line_5_1 = Line(11,22)
line_5_1(1)
print("=" * 20)
#闭包
def lin_6(k,b):
    def creat_y(x):
        print(k*x + b)
    return creat_y
line6_1 = lin_6(1,2)
line6_1(1)