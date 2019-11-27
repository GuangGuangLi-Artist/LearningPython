#coding=utf-8

import socket
import time

tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_server_socket.bind(("",8899))

tcp_server_socket.listen(128)

tcp_server_socket.setblocking(False)

client_socket_list = list()

while True:
    time.sleep(1)
    try:
        new_socket,new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print("--没有新的客户端到来--")
    else:
        print("没有异常产生，那就意味着有一个新的客户端到来")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print("这个客户端没有发送数据")
        else:
            if recv_data:
                #对方发送过来数据
                print("客户端发送过来了数据")
            else:
                #对方调用了close,导致了recv返回
                client_socket_list.remove(client_socket)
                client_socket.close()
                print("客户端已经关闭")