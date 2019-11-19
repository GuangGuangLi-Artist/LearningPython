#coding=utf-8

import multiprocessing
import time

def down_load_web(q):

    #模拟下载数据
    data = [1,2,3,4]

    #向队列中写入数据
    for i in data:
        q.put(i)
    #print("下载完毕并存入到队列")


def analysis_data(q):

    #处理数据
    waitting = list()

    #从队列中获取数据
    while True:
        data = q.get()
        waitting.append(data)

        if q.empty():
            break
    print(waitting)



def main():
    #创建一个队列
    q = multiprocessing.Queue()

    #创建多个进程，将队列的引用当作实参进行传递到里面
    p1 = multiprocessing.Process(target=down_load_web,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()