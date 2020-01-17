from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BookInfo
from django.template import loader,RequestContext

# Create your views here.
#定义视图函数，httprequest
#进行url的配置，建立url地址和视图之间的关系

def my_render(request,template_path,context_dict={}):
    temp = loader.get_template(template_path)

    # context = eval(RequestContext(request,context_dict))
    context = {temp:"temp"}

    res_html = temp.render(context)

    return  HttpResponse(res_html)


def index(request):

    #进行处理，和M和T进行交互
    #return HttpResponse('Django 学会了有什么用啊')

    #使用模板文件
    #加载模板文件，模板对象
    # temp = loader.get_template('blog/index.html')
    # #定义模板上下文，给模板文件传递数据,其中context要求是一个字典
    # context = {"temp":temp}
    # # context =Context({})
    #
    #
    # #模板渲染，产生标准的html内容
    # res_html = temp.render(context)
    #
    # #返回给浏览器
    # return HttpResponse(res_html)
    # return my_render(request,'blog/index.html')

    return render(request,'blog/index.html',{"name":"苏彪","list":list(range(1,10))})



def favoriteBook(requets):

    return HttpResponse('战争与和平')

def show_books(request):
    '''显示图书的信息'''
    #1.通过M查找图书表中的数据
    books = BookInfo.objects.all()

    #2.使用模板
    return render(request,"blog/show_books.html",{'books':books})


def detail(request,bid):
    '''查询图书关联的英雄信息'''
    #1.根据bid查询图书信息
    book = BookInfo.objects.get(id=bid)
    #2.查询和book关联的英雄信息
    heros = book.heroinfo_set.all()

    #3.使用模板
    return render(request,'blog/detail.html',{'book':book,'heros':heros})
