import random


def print_hi():
    print('Print hi!!!')


if __name__ == '__main__':
    print(random.randint(12, 123))
    my_list = [1, 2, True, 65]
    print(random.choice(my_list))
    print(type(random))
