import time
from threading import Thread

def func1():
    list_1 = list(range(1, 11))
    for i in list_1:
        print(i)
        time.sleep(1.1)

def func2():
    list_2 = [chr(x) for x in range(ord('a'), ord('j') + 1)]
    for i in list_2:
        print(i)
        time.sleep(1)

thread_1 = Thread(target=func1)
thread_2 = Thread(target=func2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

