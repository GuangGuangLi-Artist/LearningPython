#coding=utf-8

import socket

def main():

    #创建socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #目的地信息
    #server_ip = input("请输入服务器ip:")
    #server_port = int(input("请输入目的地端口:"))

    #链接服务器
    #tcp_client_socket.connect((server_ip,server_port))
    tcp_client_socket.connect(('45.76.213.222', 7890))
    #输入需要下载的文件名
    file_name = input("请输入要下载的文件名:")

    #发送文件下载请求
    tcp_client_socket.send(file_name.encode("utf-8"))

    #接收服务器发送回来的数据，一次最大接受1k(1024*1024)

    recev_data = tcp_client_socket.recv(1024*1024)

    print("接收到的数据为:",recev_data.decode("utf-8"))

    #如果接收到数据就创建文件，如果没接收，就不创建
    if recev_data:
        with open("[接收]" + file_name,"wb") as f:
            f.write(recev_data)

     #关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
    




