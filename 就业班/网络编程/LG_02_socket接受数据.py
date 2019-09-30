#coding=utf-8
import socket

def main():

    #1:创建socket对象
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #2：本机绑定端口
    local_addr = ("",7788)
    s.bind(local_addr)
    #3：接受数据
    while True:
        data = s.recvfrom(1024)  # 接受到的数据是一个元组(接收到的数据,(发送方的ip,port))
        data_msg = data[0]
        send_addr = data[1]
        #4：打印数据
        print("%s:%s" %((str(send_addr)),data_msg.decode("utf-8")))
    #关闭socket对象
    s.close()




if __name__ == "__main__":
    main()