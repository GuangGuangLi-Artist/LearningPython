#自定义过滤器
#过滤器其实就是python的函数
from django.template import Library

#创建一个Library类的对象
register = Library()


#自定义过滤器，至少有一个参数，最多两个参数
@register.filter
def mod(num):
    return num%2 ==0


@register.filter
def mod_val(num,val):
    return num%val ==0