# countdown.py
# An example of defining a thread as a class
import sys
import time
import threading

from threading import Lock, RLock

count = 10
count2 = 10
crossroad = 0


#
# class CountdownThread(threading.Thread):
#     result = True
#
#     def __init__(self, count, name, t_to_sync=None, daemon=False):
#         threading.Thread.__init__(self, name=name, daemon=daemon)
#         self.count = count
#         self.t = t_to_sync
#         self.result = False
#         self.trace = False
#
#     def join(self, timeout=None):
#         super().join()
#         return self.trace
#
#     def start(self):
#         super(CountdownThread, self).start()
#         return self.result
#
#     def run(self):
#         try:
#             print(threading.current_thread().getName())
#             while self.count > 0:
#                 print("Counting down", self.count)
#                 self.count -= 1
#                 time.sleep(1)
#             # while True:
#             #     if self.t and not self.t.is_alive():
#             #         print(self.t.is_alive(),
#             #               self.t.name)
#             #         #self.t.setDaemon(True)
#             #         break
#             #     print("Counting down", self.count)
#             #     self.count -= 1
#             #     time.sleep(0.2)
#             self.result = True
#             self.trace = True
#             return self.count
#         except Exception as exec:
#             time.sleep(1)
#             self.trace = exec


# # Sample execution
# t1 = CountdownThread(5, "Name")
# t2 = CountdownThread(10, "Thread", t1, daemon=True)
# t1.setDaemon(True)
#
# initial_res1 = t1.start()
# initial_res2 = t2.start()
#
#
# trace1 = t1.join()
# trace2 = t2.join()
#
# print("Done", t1.result, trace1, trace2)

def inner_func(data, lock):
    print("Enter to inner function")
    lock.acquire()
    for i in range(data):
        print("======>", i)
    lock.release()
    return 100


def third_th(th, lock):
    global crossroad, count2
    print('Enter thread #3')
    lock.acquire()
    count2 += second_th(lock)
    lock.release()
    time.sleep(2)

    print("after")


def second_th(lock):
    global count2, crossroad
    while count2:
        with lock:
            count2 -= 1
            print(f'---count2: {count2}')
            time.sleep(0.5)
    crossroad = 1
    return 100

lock = Lock()
rlock = RLock()
th2 = threading.Thread(target=second_th, args=(rlock,), name='second_thread', daemon=False)
th3 = threading.Thread(target=third_th, args=(th2, rlock), name='third_thread', daemon=True)

th2.start()
th3.start()


while not crossroad:
    count -= 1
    print(f'---***: {count}')
    time.sleep(0.3)

print("Done", count2)

