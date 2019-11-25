#coding=utf-8
import socket


def server_client(new_socker):
    """为这个客户端返回数据"""

    request = new_socker.recv(1024)

    print(request)

    #返回http格式的数据给浏览器
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    response += "我是大爷你"
    new_socker.send(response.encode("gbk"))

    #关闭套接字
    new_socker.close()


def main():
    #创建socket
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定
    server_socket.bind(("",8899))

    #变为监听套接字
    server_socket.listen(128)
    while True:

        #等待新的客户端的链接
        new_socket,client_addr = server_socket.accept()

        #为客户端服务
        server_client(new_socket)
    server_socket.close()


if __name__ == "__main__":
    main()


