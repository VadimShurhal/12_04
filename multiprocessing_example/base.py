import time

import multiprocessing

from multiprocessing import Process


def f(name):
    print('hello', name)
    print(f'{multiprocessing.current_process().name}')
    time.sleep(17)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p1 = Process(target=f, args=('Joe',))
    p.start()
    p1.start()
    print(p.is_alive())
    print(p.pid)
    # with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
    #     p.map(f, ['Joe', "Bob", 'Anna'])



# def task():
#     for i in range(10):
#         print(f"Hello {i}")
#         time.sleep(1)
#
#
# multiprocessing.Process(target=task, name='pr-1').start()
