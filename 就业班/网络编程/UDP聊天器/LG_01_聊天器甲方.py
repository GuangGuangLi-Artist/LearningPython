#coding=utf-8
import socket

def send_msg(s):
    """发送消息"""
    # 目标地址
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的端口："))

    # 要发送的数据
    content = input("请输入要发送的数据：")

    # 接受数据的地址
    # dest_addr = ('167.179.85.140',7788)

    # 发送数据
    s.sendto(content.encode('utf-8'), (dest_ip, dest_port))

def recv_msg(s):
    """接收数据"""
    # 接受数据
    data = s.recvfrom(1024)
    data_msg = data[0]
    send_addr = data[1]
    print("%s:%s" % ((str(send_addr)), data_msg.decode("utf-8")))



def main():
    #创建套接字对象
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定端口
    s.bind(("",8888))


    while True:
        print("***李广聊天器***")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出程序")
        op = input("请输入功能操作")
        if op == "1":
            #发送
            send_msg(s)
        elif op == "2":
            #接收
            recv_msg(s)
        elif op == "0":
            break
        else:
            print("你瞎输入啥？")

    #关闭socket
    s.close()

    print("*" * 50)


if __name__ == "__main__":
    main()