import time
import threading


def test():
    while True:
        print('test')
        time.sleep(1)


th = threading.Timer(10, test)
th.start()


while True:
    print('Main thread....')
    time.sleep(1)