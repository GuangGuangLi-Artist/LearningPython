#coding=utf-8


from flask import  Blueprint

app_cart = Blueprint("app_cart",__name__,template_folder="templates",static_folder="static")

#在__init__文件被执行的时候，把视图加载进来，让蓝图与应用程序知道有视图的存在
from .views import get_cart