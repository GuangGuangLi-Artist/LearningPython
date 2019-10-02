#coding=utf-8

import socket

def main():

    #创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定本地信息
    tcp_server.bind(("",9999))

    #让默认的套接字由主动变为被动链接
    tcp_server.listen(128)

    print("----1----")
    #等待客户端的链接
    new_client_socket,client_addr = tcp_server.accept()
    print("-----2----")

    print(new_client_socket)
    print(client_addr)

    #接收客户端发来的消息
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    new_client_socket.send("消息收到".encode("utf-8"))


    #关闭套接字
    new_client_socket.close()
    tcp_server.close()

if __name__ == "__main__":
    main()