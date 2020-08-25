

import os


def main():
    files = os.listdir("F:\\test_batch_rename")
    print(files)
    for filename in os.listdir("F:\\test_batch_rename"):
        #将文件名称按照符号进行分割
        splitfile = os.path.splitext(filename)
        #拆包
        rootname,file_ext = splitfile
        print(splitfile)



if __name__ == '__main__':
    main()