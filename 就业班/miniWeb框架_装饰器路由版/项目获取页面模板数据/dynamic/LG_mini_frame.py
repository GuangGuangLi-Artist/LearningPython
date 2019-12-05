

"""
URL_FUNC_DICT = {
    "/index.html":login,
    "/center.html":center
}
"""

URL_FUNC_DICT = dict()

def route(url):#<<<<------------添加的装饰器
    def set_func(func):
        URL_FUNC_DICT[url] = func
        print(URL_FUNC_DICT)
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func

@route("/login.html")#<<<<------------带参数的装饰器
def login():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content

@route("/center.html")
def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    return content





def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH"]
    print(file_name)

    """
    if file_name == "/login.py":
        return login()
    elif file_name == "/center.py":
        return center()
    else:
        return "Hello World _我是开发者李广先生"
    """
    try:
        func = URL_FUNC_DICT[file_name]
        return func()
        #URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常: %s" % str(ret)




