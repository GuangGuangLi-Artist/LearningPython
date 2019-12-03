#coding=utf-8
import socket
import multiprocessing
import re
import dynamic.LG_mini_frame


class WSGIServer():

    def __init__(self):
        # 创建socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置当服务器先close,即服务器四次挥手之后能够立即释放资源，这样就保证了，下次程序运行时，能够立即绑定8899端口
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        self.server_socket.bind(("", 8899))

        # 变为监听套接字
        self.server_socket.listen(128)


    def server_client(self,new_socker):
        """为这个客户端返回数据"""

        request = new_socker.recv(1024).decode("utf-8")

        request_lines = request.splitlines()
        print(request_lines)

        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        #print(ret)
        file_name = ""
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"

        # response += "我是大爷你"
        if not file_name.endswith(".py"):
            try:
                #f = open(r"F:\传智python\课件资料\05python和linux高级编程阶段\1-6代码和截图\08-http服务器的实现-2\代码\html" + file_name, "rb")
                f = open("./static" + file_name, "rb")
                # f = open(r"D:/video/传智python/课件资料/05python和linux高级编程阶段/1-6代码和截图/07-http协议、http服务器的"
                #          r"实现-1/代码/html" + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "file not found"
                new_socker.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 返回http格式的数据给浏览器
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socker.send(response.encode("utf-8"))
                new_socker.send(html_content)
        else:
            env = dict()
            env["PATH"] = file_name
            body = dynamic.LG_mini_frame.application(env,self.set_response_header)
            print(self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                header += "%s:%s\r\n" %(temp[0],temp[1])

            header += "\r\n"
            response = header + body
            #print(response)
            new_socker.send(response.encode("utf-8"))

        # 关闭套接字
        new_socker.close()

    def set_response_header(self,status,headers):
        self.status = status
        self.headers = [("server","mini_web V1.1")]
        self.headers += headers

    def run_forever(self):
        while True:
            # 等待新的客户端的链接
            new_socket, client_addr = self.server_socket.accept()

            # 为客户端服务
            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            p.start()
            new_socket.close()
            # server_client(new_socket)
        self.server_socket.close()
def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()


