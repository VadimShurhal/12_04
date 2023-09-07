import time
import threading


def first(sec):
    time.sleep(sec)
    print('First function ')


def second(sec):
    time.sleep(sec)
    print('Second function ')


def third(sec):
    time.sleep(sec)
    print('Third function ')


first = threading.Thread(target=first, args=(4,), name='first')
first.start()
second = threading.Thread(target=second, args=(2,), name='second')
second.start()
third = threading.Thread(target=third, args=(3,), name='third')
third.start()
