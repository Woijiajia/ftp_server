"""
练习:
模拟会场出票系统 , 现有有 500张票 记为 (T1 .... T500)
由于票的顺序涉及到座位排布,所以票必须按照顺序卖出
有10个窗口(w1--w10)同时买票,每张票出票时间为 0.1秒.
按照上述描述使用多线程完成,每个线程代表一个窗口,将票卖出,直到所有票卖完
卖出时打印下哪个窗口卖了哪张

w1 --- T48
"""

from threading import Thread,Lock
from time import sleep

lock = Lock()  # 锁对象
ticket = ["T%d"%x for x in range(1,501)]  # 存储车票

# 买票过程
def sell(w):
    """
    :param w: 窗口名称
    """
    while True:
        sleep(0.1)
        lock.acquire()
        if not ticket:
            lock.release()
            break
        print("%s窗口卖出:%s"%(w,ticket.pop(0)))
        lock.release()

    print("余票不足")

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=('W%d'%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]






