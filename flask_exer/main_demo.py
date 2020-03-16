#coding=utf-8

from flask import  Flask
#解决循环引用的方式:方式1,推迟一方的导入，让另一方先完成;方式2:在主函数直接调用装饰器装饰定义的函数
from goods_demo import get_goods
from users_demo import register
from orders_demo import app_orders
from cart import app_cart

app = Flask(__name__)
app.route("/get_goods")(get_goods)
app.route("/register")(register)


#注册蓝图
# app.register_blueprint(app_orders)
app.register_blueprint(app_orders,url_prefix="/orders")
app.register_blueprint(app_cart,url_prefix="/cart")

#装饰器不止可以在函数之前使用，也可以在函数定义之后使用

@app.route("/")
def index():
    return "index page"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)