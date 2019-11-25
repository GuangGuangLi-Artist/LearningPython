#coding=utf-8

import re

def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def main():
    yuedu_str = "阅读次数为:999"
    ret1 = re.search("\d+",yuedu_str)
    print(ret1.group())

    yuedu_all_str = "python:999,c++:888,java:10000"
    ret2 = re.findall("\d+",yuedu_all_str)
    print(ret2)

    tihuan_str = "python=888"
    ret3 = re.sub(r"\d+","999",tihuan_str)
    print(ret3)

    ret4 = re.sub(r"\d+",add,tihuan_str)
    print(ret4)



if __name__ == "__main__":
    main()