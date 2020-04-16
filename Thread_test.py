"""
线程效率
"""

import time
from threading import Thread
from multiprocessing import Process

def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

tm = time.time()
# for i in range(10):
#     count(1,1)

jobs = []
for i in range(10):
    t = Process(target = count,args=(1,1))
    jobs.append(t)
    t.start()
for i in jobs:
    i.join()

# 用时: 9.348727703094482
# 用时: 7.692718744277954
# 用时: 5.902653455734253
print("用时:",time.time() - tm)
