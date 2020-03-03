#coding=utf-8


import pandas as pd

def run():
    t2 = pd.Series([1,23,22,3,45,4,56,90])
    t3 = pd.Series([1,23,22,3,45,4,56,90],index=list("abcdefgh"))
    temp_dict = {"name":"liguang","age":"0","tel":"123456"}
    t4 = pd.Series(temp_dict)
    print(type(t2))
    print(t2)
    print("*"*20)
    print(t3)
    print("*" * 20)
    print(t4)
if __name__ == '__main__':
    run()