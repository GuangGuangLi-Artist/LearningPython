#coding=utf-8
import socket


def main():
    #创建套接字对象
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定端口
    local_addr = ("", 8888)
    s.bind(local_addr)


    while True:
    #要发送的数据
        content = input("请输入要发送的数据：")
        if content == "exit":
            break


        #接受数据的地址
        dest_addr = ('167.179.85.140',7788)

        #发送数据
        s.sendto(content.encode('utf-8'),dest_addr)


    #关闭socket
    s.close()

    print("*" * 50)


if __name__ == "__main__":
    main()