"""
练习:  有两个分之线程,同时运行,一个线程打印 1--52 这52个数字,另一个线程打印
A--Z 26个字符, 要求最终打印顺序是12A34B56C ....5152Z
"""

from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()

def print_char():
    # A--Z对应的数字
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_char)

lock2.acquire()

t1.start()
t2.start()
t1.join()
t2.join()