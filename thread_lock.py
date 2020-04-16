"""
线程锁示例
"""
from threading import Thread,Lock

a = b = 0
lock = Lock() # 生成锁对象


# 线程函数
def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()  # 解锁

t = Thread(target=value)
t.start()

while True:
    lock.acquire()  # 上锁
    a += 1
    b += 1
    lock.release() # 解锁

t.join()