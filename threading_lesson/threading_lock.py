import time
import threading


value = 0
locker = threading.Lock()
# rlock = threading.RLock()
# with locker


def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(0.5)
        print(value)
        # locker.release()


# for _ in range(5):
#     threading.Thread(target=inc_value).start()

th1 = threading.Thread(target=inc_value, name='th1').start()
th2 = threading.Thread(target=inc_value, name='th2').start()

