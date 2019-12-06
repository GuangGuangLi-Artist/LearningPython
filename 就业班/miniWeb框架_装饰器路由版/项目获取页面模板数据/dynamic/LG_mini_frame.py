#coding=utf-8
import re
from pymysql import connect

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

@route("/index.html")#<<<<------------带参数的装饰器
def index():
    with open("./templates/index.html",encoding="utf-8") as f:
        content = f.read()

    conn = connect(host="localhost",user="root",password="123456",database="stock_db",charset="utf8")
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>
        """
    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7])
    #content = re.sub(r"\{%content%\}",str(stock_infos),content)
    content = re.sub(r"\{%content%\}", html, content)
    return content

@route("/center.html")
def center():
    with open("./templates/center.html",encoding="utf-8") as f:
        content = f.read()
    conn = connect(host="localhost",user="root",password="123456",database="stock_db",charset="utf8")
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
            </td>
        </tr>
            """
    html = ""
    for line_info in stock_infos:
        html += tr_template % (
        line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6])
    # content = re.sub(r"\{%content%\}",str(stock_infos),content)
    content = re.sub(r"\{%content%\}", html, content)
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




