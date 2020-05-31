#coding=utf-8

from itertools import islice

def file_iter():
    file_txt = open('../day02/use_file/user_file.txt')
    #迭代获取整个文本文件，使用逐行迭代的方式
    # for data in file_txt:
    #     print(data)

    #获取文件的切片行数 (100到300行数之间)
    data = islice(file_txt,100,300)

    #表示切片前500行
    # data = islice(file_txt, 300)

    #表示切片100行到文件末尾
    # data = islice(file_txt,100,None)


    return data



if __name__ == '__main__':
    data_res = file_iter()
    for x in data_res:
        print(x)