
def login():
    return "这是登陆页面"

def register():
    return "这是注册页面"


def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH"]
    if file_name == "/login.py":
        return login()
    elif file_name == "/register.py":
        return register()
    else:
        return "Hello World _我是开发者李广先生"




