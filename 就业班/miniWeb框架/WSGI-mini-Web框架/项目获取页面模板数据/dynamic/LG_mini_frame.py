
def login():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()
    return content
def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    return content


def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    file_name = environ["PATH"]
    if file_name == "/login.py":
        return login()
    elif file_name == "/center.py":
        return center()
    else:
        return "Hello World _我是开发者李广先生"




