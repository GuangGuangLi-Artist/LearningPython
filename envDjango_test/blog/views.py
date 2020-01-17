from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext

# Create your views here.
#定义视图函数，httprequest
#进行url的配置，建立url地址和视图之间的关系

def index(request):

    #进行处理，和M和T进行交互
    #return HttpResponse('Django 学会了有什么用啊')

    #使用模板文件
    #加载模板文件，模板对象
    temp = loader.get_template('blog/index.html')
    #定义模板上下文，给模板文件传递数据
    context = RequestContext(request, {})

    #模板渲染，产生标准的html内容
    res_html = temp.render(context)

    #返回给浏览器
    return HttpResponse(res_html)



def favoriteBook(requets):

    return HttpResponse('战争与和平')