#coding=utf-8

from flask import Flask,current_app
import demo

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__,
            static_url_path="/python", #访问静态资源的url前缀，默认是static
            static_folder = "static",#静态文件的目录
            template_folder="templates",#模板文件的目录
            )

#1引入配置文件
#app.config.from_pyfile("config.cfg")
# app.config.from_pyfile("config.cfg")
#2使用对象配置参数
class Config(object):
    DEBUG = True
    ITCAST = "subiao"
app.config.from_object(Config)

#3直接操作config的字典对象
# app.config["DEBUG"] = True

# app = Flask("abcde")
@app.route('/index')
def index():
    '''定义视图函数'''
    # a = 1 / 0

    #1直接读取
    #print(app.config.get("ITCAST"))

    #2通过current_app获取
    print(current_app.config.get("ITCAST"))

    return  "hello flask"





if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0",port="5000",debug=True)