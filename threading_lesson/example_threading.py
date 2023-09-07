import threading
import time


def my_func(a):
    while True:
        print(f"{threading.current_thread().name} with param {a}")
        time.sleep(1)


thr = threading.Thread(target=my_func, args=({'name': 'Joe'}), name='My thread')
thr.start()

thr2 = threading.Thread(target=my_func, args=({'name': 'Joe'}), name='My second thread')
thr2.start()

for i in range(20):
    print(f"My iteration {i}")
    time.sleep(1)

    if i % 3:
        print('active thread count', threading.active_count())
        print('thread count', threading.enumerate())
        print('Is alive', thr.is_alive())



