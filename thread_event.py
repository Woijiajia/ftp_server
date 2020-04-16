"""
event 线程同步互斥方法
"""

from threading import Thread,Event

s = None
e = Event()  # event对象

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 解除主线程的阻塞

t = Thread(target=杨子荣)
t.start()

e.wait()  # 阻塞等待
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人")
else:
    print("打死他,无情啊")

t.join()
