#coding=utf-8

#把元组用作记录
lax_coordinates = (33.9425,-118.408056)
city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print("%s/%s" %passport)


#for循环分别提取元组里的元素,也叫做拆包,可以使用“_”作为占位符
for country,_ in traveler_ids:
    print(country)


for country_1,passport_num in traveler_ids:
    print(country_1,passport_num)
    print(country_1)
    print(passport_num)