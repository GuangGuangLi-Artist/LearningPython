#coding=utf-8

class Goods(object):

    def __init__(self):

        self.origin_price = 100

        self.disaccount = 0.8

    @property
    def price(self):
        new_price = self.origin_price * self.disaccount
        return new_price

    @price.setter
    def price(self,value):
        self.origin_price = value

    @price.deleter
    def price(self):
        del self.origin_price



def main():
    obj = Goods()
    obj.price         # 获取商品价格
    obj.price = 200   # 修改商品原价
    del obj.price     # 删除商品原价

if __name__ == "__main__":
    main()
