# coding=utf-8

def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

#demo(1)
#demo(1,2,3,4)
demo(1,2,3,4,5,name="李广",age=18)