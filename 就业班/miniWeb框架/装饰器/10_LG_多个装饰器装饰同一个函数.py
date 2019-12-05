#coding=utf-8


def set_func_1(fun):
    def call_fun():
        return "<h1>" + fun() + "</h1>"
    return call_fun


def set_func_2(fun):
    def call_fun():
        return "<br>" + fun() + "</br>"
    return call_fun



@set_func_1
@set_func_2
def get_str():
    return "hahha"

print(get_str())


#装饰器哪个装饰器在前面，那么哪个就先执行