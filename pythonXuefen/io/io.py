#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from io import StringIO
from io import BytesIO

'''
文件读写
    写文件

    读文件
        read() 调用read()方法可以一次读取文件的全部内容
        readline()可以每次读取一行内容
        readlines()一次读取所有内容并按行返回list


'''

file_path = os.getcwd() + '\\io\\for_read'


with open(file=file_path,mode='w') as f:
    f.write('hello world \nhello liguang')

with open(file=file_path,mode='r') as f:
    str = f.read()
    print(str)


print('---------------')
with open(file=file_path,mode='r') as f:
    flist = f.readlines()#一次读取所有内容并按行返回list
    for str in flist:
        print(str)
print('---------------')
for line in open(file=file_path,mode='r'):
    print(line) #一次读取一行

print('---------------')

fio = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = fio.readline()
    if s == '':
        break
    print(s.strip())
print('---------------')
fbo = BytesIO()
fbo.write('李哈哈'.encode('utf-8'))
print(fbo.getvalue())
print('---------------')
def test_os():
    print(os.name) # 操作系统类型
    print(os.environ) #环境变量
    print(os.environ.get('PATH'))

    print('当期目录的绝对路径 %s' %(os.path.abspath('.')))
    # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来 然后创建一个目录:
    os.path.join('F:\pycharmWorkspace\pythonXuefen','io_os')
    os.mkdir('F:\pycharmWorkspace\pythonXuefen\io_os')
    os.rmdir('F:\pycharmWorkspace\pythonXuefen\io_os')

test_os()
