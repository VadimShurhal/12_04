from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Start task with {id=}...')
    sleep(1)
    print(f'Finished task {id=} ')


start_time = perf_counter()

threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()

print(f'Time to execute {end_time- start_time: 0.2f} second.')