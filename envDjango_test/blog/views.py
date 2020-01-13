from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#定义视图函数，httprequest
#进行url的配置，建立url地址和视图之间的关系

def index(request):

    #进行处理，和M和T进行交互
    return HttpResponse('Django 学会了有什么用啊')


def favoriteBook(requets):

    return HttpResponse('战争与和平')