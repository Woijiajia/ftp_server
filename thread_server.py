"""
多线程并发模型
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 应对客户端请求
def handle(connfd):
    # 处理客户端请求的请求 (长期处理)
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data)
        connfd.send(b'OK')
    connfd.close()

def main():
    # 创建套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(3)

    print("Listen the port 8888")
    # 循环链接客户端
    while True:
        try:
            connfd,addr = sock.accept()
            print("客户端地址:",addr)
        except:
            sys.exit("服务退出")

        # 创建新的线程,处理客户端请求  handle --> 具体处理请求函数
        t = Thread(target = handle,args = (connfd,))
        t.setDaemon(True)  # 主服务退出,其他服务也随之退出
        t.start()



if __name__ == '__main__':
    main()