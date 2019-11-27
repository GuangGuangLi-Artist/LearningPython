#coding=utf-8
import socket
import gevent
from gevent import monkey
import re

monkey.patch_all()


def server_client(new_socker):
    """为这个客户端返回数据"""

    request = new_socker.recv(1024).decode("utf-8")

    request_lines = request.splitlines()
    print(request_lines)

    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"


    # response += "我是大爷你"
    try:
        f = open(r"D:/video/传智python/课件资料/05python和linux高级编程阶段/1-6代码和截图/07-http协议、http服务器的"
             r"实现-1/代码/html" + file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "file not found"
        new_socker.send(response.encode("gbk"))
    else:
        html_content = f.read()
        f.close()
        # 返回http格式的数据给浏览器
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socker.send(response.encode("gbk"))
        new_socker.send(html_content)

    #关闭套接字
    new_socker.close()


def main():
    #创建socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置当服务器先close,即服务器四次挥手之后能够立即释放资源，这样就保证了，下次程序运行时，能够立即绑定8899端口
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #绑定
    server_socket.bind(("",8899))

    #变为监听套接字
    server_socket.listen(128)
    while True:

        #等待新的客户端的链接
        new_socket,client_addr = server_socket.accept()

        #为客户端服务
        gevent.spawn(server_client,new_socket)
        #new_socket.close()
        #server_client(new_socket)
    server_socket.close()


if __name__ == "__main__":
    main()


