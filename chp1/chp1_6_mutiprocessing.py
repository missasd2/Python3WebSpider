"""
https://cuiqingcai.com/3335.html
Python 爬虫进阶六之多进程的用法
"""

from multiprocessing import Process
import time, os

def f(name):
    print("hello", name)


"""
显示所涉及的各个进程ID，这是一个扩展示例：
"""
def info(title):
    print(title)
    print("module name: ", __name__)
    print("parent process: ", os.getppid())
    print("prcess id: ", os.getpid())

if __name__ == "__main__":
    for i in range(5):
        p = Process(target=f, args=(i, ))
        #time.sleep(10)
        p.start()
    p.join()
    
    q = Process(target=info, args=("lui", ))
    q.start()