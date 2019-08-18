# coding=utf-8


class HouseItem():

    def __init__(self,name,area):

        self.name = name
        self.area =area

    def __str__(self):

        return "[%s]占地%.2f平方米"%(self.name ,self.area)


class House():

    def __init__(self,house_type,area):

        self.house_type = house_type
        self.area = area

        #剩余面积
        self.free_area = area

        #家具列表
        self.item_list = []

    def __str__(self):
        return "户型:%s\n总面积:%2.f [剩余:%2.f]\n家具:%s" \
               %(self.house_type,self.area,
                 self.free_area,self.item_list)

    #添加家具
    def add_item(self,item):
        print("要添加%s" %item)

        #判断家具的面积
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加" %item.name)
            return

        #将家具的名称添加到列表中
        self.item_list.append(item.name)

        #输出剩余面积
        self.free_area -= item.area



bed = HouseItem("席梦思",40)
chest = HouseItem("衣柜",2)
table = HouseItem("餐桌",20)
print(bed)
print(chest)
print(table)

#创建房子
my_house = House("两室一厅",60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)