#coding=utf-8

from random import randint
from itertools import chain


class Iter_Exer():

    def bingxing_iter(self):
        chinese_score = [randint(60,100) for i in range(40)]
        math_score = [randint(60,100) for i in range(40)]
        english_score = [randint(60,100) for i in range(40)]

        #求每个学生的总分
        total_score = []
        for cs,ms,es in zip(chinese_score,math_score,english_score):
            total_score.append(cs+ms+es)

        return total_score


    def chaungxing_iter(self):
        #各个班级的成绩表和人数
        class_1 = [randint(60,100) for x in range(40)]
        class_2 = [randint(60,100) for x in range(42)]
        class_3 = [randint(60,100) for x in range(45)]
        class_4 = [randint(60,100) for x in range(39)]
        #计算分数超过90分的人
        count = 0
        for i in chain(class_1,class_2,class_3,class_4):
            if  i > 90:
                count += 1
        return count

if __name__ == '__main__':
    ie = Iter_Exer()

    tatal_res = ie.bingxing_iter()
    print(tatal_res)

    print("*" * 50)
    count_res = ie.chaungxing_iter()
    print(count_res)

