#coding=utf-8

class Goods(object):


    def __init__(self):
        self.origin_price = 100
        self.discount = 0.8

    def get_price(self):
        new_price = self.origin_price * self.discount
        return new_price

    def set_price(self,value):
        self.origin_price = value


    def del_price(self):
        del self.origin_price


    PRICE = property(get_price,set_price,del_price,'价格属性描述')

obj = Goods()
p = obj.PRICE
print(p)

obj.PRICE = 200
p1 = obj.PRICE
print(p1)

del obj.PRICE