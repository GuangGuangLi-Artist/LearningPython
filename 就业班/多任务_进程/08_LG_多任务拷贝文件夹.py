#coding=utf-8

import multiprocessing
import time
import os


def copy_files(q,file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""
    #print("====>模拟copy文件: 从%s--->到%s 文件名是%s" % (old_folder_name,new_folder_name,file_name))
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    #如果拷贝结束，就向队列写入一个消息，表示已经完成
    q.put(file_name)



def main():
    """这是一个文件夹拷贝脚本"""
    #获取用户要拷贝的文件夹的名字
    old_folder_name = input("请输入要拷贝的文件夹的名字:")


    #创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    #获取文件夹中需要copy的文件的名字
    file_names = os.listdir(old_folder_name)
    #print(file_names)


    #创建进程池
    po = multiprocessing.Pool(5)

    #创建一个队列
    q = multiprocessing.Manager().Queue()

    #向进程池添加拷贝文件的任务
    for file_name in file_names:
        po.apply_async(copy_files,args=(q,file_name,old_folder_name,new_folder_name))

    po.close()
    #po.join()
    #显示拷贝进度
    all_file_num = len(file_names)
    copy_ok = 0
    while True:
        file_name = q.get()
        copy_ok+=1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok *100/ all_file_num),end="")
        #回到行首
        if copy_ok >= all_file_num:
            break
    print()


if __name__ == "__main__":
    main()