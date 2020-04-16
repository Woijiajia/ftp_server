"""
多进程并发模型
重点代码

整体步骤:
创建网络套接字用于接收客户端请求
循环等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""

from socket import *
from multiprocessing import Process
from signal import *
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

    # 处理僵尸进程
    signal(SIGCHLD,SIG_IGN)

    print("Listen the port 8888")
    # 循环链接客户端
    while True:
        try:
            connfd,addr = sock.accept()
            print("客户端地址:",addr)
        except:
            sys.exit("服务退出")

        # 创建子进程,处理客户端请求  handle --> 具体处理请求函数
        p = Process(target = handle,args = (connfd,))
        p.daemon = True  # 主服务退出,其他服务也随之退出
        p.start()



if __name__ == '__main__':
    main()










