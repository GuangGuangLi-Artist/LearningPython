#coding=utf-8

import socket

def main():


    #创建tcp协议的socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #链接服务器
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))
    server_addr = (server_ip,server_port)
    s.connect(server_addr)

    #发送数据
    send_data = input("请输入你要发送的数据：")
    s.send(send_data.encode("utf-8"))


    #关闭套接字
    s.close()



if __name__ == "__main__":
    main()