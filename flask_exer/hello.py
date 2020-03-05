#coding=utf-8

from flask import Flask

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
@app.route('/index')
def index():
    '''定义视图函数'''
    return  "hello flask"





if __name__ == '__main__':
    app.run()