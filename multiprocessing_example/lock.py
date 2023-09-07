import time

import multiprocessing

lock = multiprocessing.Lock()


def get_value(l):
        l.acquire()
        print(f"{multiprocessing.current_process()} - {time.time()}")
        time.sleep(1)


pr = multiprocessing.Process(target=get_value, args=(lock, ), name='pr-1')

pr.start()
