from threading import Timer
import uuuu


def hello():
    print("执行结束")
    print(uuuu.un(), '执行结束')


t = Timer(10.0, hello)
t.start()
