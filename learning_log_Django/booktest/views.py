#导入重定向函数
from django.shortcuts import render,redirect
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.

def index(request):
    '''显示图书信息'''
    #1查询所有的图书信息
    books = BookInfo.objects.all();
    #2使用模板

    return render(request,'booktest/index.html',{'books':books})


def create(request):
    '''新增一本图书'''
    #创建对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,2,1)
    b.save()

    #返回应答,让浏览器再访问/index,重定向
    #return HttpResponseRedirect('/index')
    return redirect('/index')


def delete(request,bid):
    '''删除点击的图书'''
    #1通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    #2删除
    book.delete()
    #3重定向到首页/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')


def error(request):
    #制造服务器返回500
    err = 'a' + 1

    return render(request,'booktest/index.html')

def show_num(request,num):
    return HttpResponse(num)

def show_namenum(request,num):
    return HttpResponse(num)


def login(request):
    return render(request,'booktest/login.html')


def login_check(request):
    #获取提交的用户名和密码
    #request.POST   class 'django.http.request.QueryDict'
    #request.GET    class 'django.http.request.QueryDict'
    username = request.POST.get('username')
    password = request.POST.get('password')

    # print(type(request.POST))

    #进行登陆校验
    if username == 'liguang' and password == '123456':
        return redirect('/index')
    else:
        return redirect('/login')
    #返回应答
    # return HttpResponse('ok')

def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    return JsonResponse({'res':1})



