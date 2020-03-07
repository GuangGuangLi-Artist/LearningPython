#coding=utf-8

from flask import Flask,current_app,redirect,url_for
from werkzeug.routing import BaseConverter

# 创建flask对象
# __name__表示当前模块的名字
app = Flask(__name__)
#转换器
#http://127.0.0.1:5000/goods/123
@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):
    '''定义视图函数'''

    return  "goods_detail %s" %goods_id
    #goods_detail 123

#1定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super().__init__(url_map)
        self.regex = r'1[34578]\d{9}'


class RegexConvertter(BaseConverter):
    def __init__(self,url_map,*args):
        #调用父类的初始化方法
        super(RegexConvertter,self).__init__(url_map)
        #将正则表达式的参数保存到对象的属性中，flask回去使用这个属性来进行路由的正则匹配
        self.regex = args[0]

    def to_python(self, value):
        print("to_python被调用")
        return str(value)

    def to_url(self, value):
        '''使用url_for的时候被调用'''
        pass

#2设置将自定义的转换器添加到flask应用中
app.url_map.converters["re"] = RegexConvertter
app.url_map.converters["mobile"] = MobileConverter

#3使用

# @app.route("send/<mobile:mobile_num>")
@app.route('/send/<re(r"1[34578]\d{9}"):mobile_num>')
def send_sms(mobile_num):
    return "send_sms to %s" %mobile_num


if __name__ == '__main__':

    #查看flask的路由信息
    print(app.url_map)
    app.run(debug=True)