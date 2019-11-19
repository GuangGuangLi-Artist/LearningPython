#coding=utf-8
from multiprocessing import Pool
import os,time,random

def log_time(task_name):
    print('Run task %s (%s)...' % (task_name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (task_name, (end - start)))
    # print("%s开始执行，进程号为%d" %(task_name,os.getppid()))
    # t_start = time.time()
    # time.sleep(random.random()*5)
    # t_stop = time.time()
    # print(str(task_name) + "执行完毕，耗时%0.2f" %(t_stop - t_start))



if __name__ ==  '__main__':
    # print("Parent process %s " % os.getpid())
    # p = Pool(4)
    # for i in range(5):
    #     p.apply_async(log_time,args=(i,))
    #
    # print("---start---")
    # p.close()
    # p.join()
    # print("---end---")

    print('Parent process %s.' % os.getpid())
    # 核心进程数
    p = Pool(3)
    for i in range(10):
        # 创建子进程
        p.apply_async(log_time, args=(i,))
    print('Waiting for all subprocesses done...')
    # 关闭进程池，关闭后不能添加新的子进程
    p.close()
    # 进程间同步，子进程运行完成后，代码继续执行
    p.join()
    print('All subprocesses done.')