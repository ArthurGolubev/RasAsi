from threading import Thread
import time


def d1():
    print('start d1')
    time.sleep(20)
    raise EOFError

def d2():
    while True:
        if not t1.is_alive():
            t1.join()
            t3.start()
            time.sleep(5)
            print('ok')

t1 = Thread(target=d1, name='d1')
t3 = Thread(target=d1, name='d1')
t2 = Thread(target=d2, name='d2')

t1.start()
t2.start()
