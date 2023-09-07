import threading

data = threading.local()


def get():
    data.value = 'test'
    print(data.value)


def t1():
    data.value = {'name': 'Joe'}
    print(data.value)


def t2():
    data.value = [1, 23, 55]
    print(data.value)


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()

get()
