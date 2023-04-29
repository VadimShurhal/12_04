import os


# print(os.getcwd())

# print(os.cpu_count())

#
# for _ in range(1, 10):
#     print(os.mkdir(f'test_{_}'))


print(os.scandir('.'))
for item in os.scandir('.'):
    new_item: os.DirEntry = item
    print(item.name)
    # print(item.path)

# os.mkdir('hello')
# os.remove('hello')

import shutil

shutil.rmtree('hello')