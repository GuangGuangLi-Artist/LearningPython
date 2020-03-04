#coding=utf-8


import pandas as pd
import numpy as np
import string

def run():
    d1 = {"name":["xiaoming","subiao"],"age":[23,34],"tel":["100","101"]}
    d2 = [{"name":"subiao","age":34,"tel":"101"},{"name":"haha","tel":100},{"name":"kakak","age":23}]
    d3 = pd.DataFrame(np.arange(12).reshape((3,4)),index=list(string.ascii_uppercase[:3]),columns=list(string.ascii_uppercase[-4:]))
    data = pd.DataFrame(d1)
    data_1 = pd.DataFrame(d2)
    data_2 = pd.DataFrame(d3)
    print(data)
    print("*" * 20)
    print(data_1)
    print("*" * 20)
    print(data_2)
    print("*" * 20)
    print(data_2.loc["A","Z"])
    print("*" * 20)
    print(data_2.loc[:,"Y"])
    print("*" * 20)
    print(data_2.loc["A",])
    print("*" * 20)
    print(data_2.loc[["A","C"],["W","Z"]])
    print("*" * 20)
    print(data_2.iloc[0,:])
    print("*" * 20)
    print(data_2.iloc[:,0])
    print("*" * 20)
    print(data_2.iloc[1:,:2])




if __name__ == '__main__':
    run()