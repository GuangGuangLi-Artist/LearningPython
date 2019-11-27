#coding=utf-8
import socket
import re


def server_client(new_socker,request):
    """为这个客户端返回数据"""

    #request = new_socker.recv(1024).decode("utf-8")

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

        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" %len(response_body)
        response_header += "\r\n"
        response = response_header.encode("gbk") + response_body
        new_socker.send(response)

    #关闭套接字
    #new_socker.close()  变为长连接需要注释掉这个


def main():
    #创建socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #设置当服务器先close,即服务器四次挥手之后能够立即释放资源，这样就保证了，下次程序运行时，能够立即绑定8899端口
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    #绑定
    server_socket.bind(("",8899))

    #变为监听套接字
    server_socket.listen(128)
    server_socket.setblocking(False)  #设置为非堵塞
    client_socket_list = list()
    while True:

        #等待新的客户端的链接
        try:
            new_socket,client_addr = server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("gbk")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    server_client(client_socket,recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

        #为客户端服务
        #server_client(new_socket)
    server_socket.close()


if __name__ == "__main__":
    main()


