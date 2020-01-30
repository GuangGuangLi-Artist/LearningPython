#导入重定向函数
from django.shortcuts import render,redirect
from booktest.models import BookInfo,AreaInfo
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from datetime import datetime,timedelta
from django.core.paginator import Paginator
# Create your views here.


def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        if request.session.has_key('islogin'):
            #用户已登录，调用对应的函数
            return view_func(request,*view_args,**view_kwargs)
        else:
            return redirect('/login')
    return wrapper

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

    #判断用户是否登陆
    if request.session.has_key('islogin'):
        return redirect('/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request,'booktest/login.html',{'username':username})


def login_check(request):
    #获取提交的用户名和密码
    #request.POST   class 'django.http.request.QueryDict'
    #request.GET    class 'django.http.request.QueryDict'

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    #
    #
    #
    #
    #
    # # print(type(request.POST))
    #
    # #进行登陆校验
    # if username == 'liguang' and password == '123456':
    #     return redirect('/index')
    # else:
    #     return redirect('/login')
    #返回应答
    # return HttpResponse('ok')

    #ajax登陆校验
    username = request.POST.get('username')
    password = request.POST.get('password')

    #获取书否需要记住用户名
    remember = request.POST.get('remember')
    print(remember)

    if username == 'liguang' and password == '123456':
        #先判断是否需要记住用户名
        response = JsonResponse({'res':1})
        if remember == 'on':
            response.set_cookie('username',username,max_age=7*24*3600)
        request.session['islogin'] = True
        return response
    else:
        return JsonResponse({'res':0})#ajax的请求在后台，需要返回json,千万不要重定向


def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    return JsonResponse({'res':1})


def set_cookie(request):
    response = HttpResponse('设置cookie')

    response.set_cookie('num',1,max_age=14*24*3600)
    # response.set_cookie('num',2,expires=datetime.now()+timedelta(days=14))

    return response



def get_cookie(request):

    num = request.COOKIES['num']
    return HttpResponse(num)

def set_session(request):
    request.session['username'] = 'liguang'
    request.session['age'] = 18
    return HttpResponse('设置session')

def get_session(request):
    username = request.session['username']
    age = request.session['age']


    return HttpResponse(username + ':' + str(age))


def clear_session(request):
    request.session.clear()
    return HttpResponse('清除session成功')

def show_index2(request):
    return render(request,'booktest/index2.html')


def temp_var(request):
    '''模板变量'''
    my_dict = {'title':'字典键值'}
    my_list = [1,2,3]
    book = BookInfo.objects.get(id=1)
    context = {'my_dict':my_dict,'my_list':my_list,'book':book}

    return  render(request,'booktest/temp_var.html',context)


def temp_inherit(request):
    '''模板继承'''
    return render(request,'booktest/child.html')


def html_escape(request):
    return render(request,'booktest/html_escape.html',{'content':'<h1>hello</h1>'})


def url_reverse(request):
    return render(request,'booktest/url_reverse.html')

@login_required
def change_pwd(request):
    '''显示修改密码页面'''
    # if not request.session.has_key('islogin'):
    #     return

    return render(request,'booktest/change_pwd.html')

@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''

    #获取新密码
    pwd = request.POST.get('pwd')
    username = request.session.get('username')
    return HttpResponse('%s修改密码为:%s'%(username,pwd))


def show_area(request,pindex):
    '''分页'''
    #查询出所有省级的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    #分页
    paginator = Paginator(areas,10)
    print(paginator.num_pages)
    print(paginator.page_range)
    if pindex == '':
        pindex = 1
    else:
        pindex = int(pindex)
    page = paginator.page(int(pindex))
    print(page.number)

    return  render(request,'booktest/show_area.html',{'page':page})


def areas(request):
    return render(request,'booktest/areas.html')


def prov(request):
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    areas_list = []
    for area in areas:
        areas_list.append((area.id,area.atitle))

    return JsonResponse({'data':areas_list})



def city(request, pid):
    '''获取pid的下级地区的信息'''
    # 1.获取pid对应地区的下级地区
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)

    # 2.变量areas并拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 3.返回数据
    return JsonResponse({'data': areas_list})






