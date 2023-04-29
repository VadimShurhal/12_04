# from random_task import print_hi
#
#
# if __name__ == '__main__':
#     print_hi()

# python mail.py --path /user/bin/file.pdf


# git status
# git add
# git add . add all files
# git add Lesson_6/random_task.py
# git commit -m "some text"
# git push

# def get_max_number(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# # print(get_max_number(11, 12))
#
# max_value = get_max_number(110, 12)
# print(max_value)


# def get_max_number(a, b=10):
#     if a > b:
#         return a
#     else:
#         return b
#
# value = get_max_number(7, 6)
# print(value)


# def get_max_number(a, b=10):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(get_max_number(b=11, a=5))


# def get_max_number(a, b=10):
#     if a > b:
#         return a, True
#     else:
#         return b, False
#
# values = get_max_number(2,4)
# print(type(values))
# print(values)
#
# value, is_true = values
# print(value, is_true)


# *args -> tuple()
# **kwargs -> dict()

# def get_max_number(age, type, *numbers, lesson=1, **addition_params):
#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     if addition_params.get('lesson') == 5:
#         print(addition_params['my_name'])
#     print(age)
#     print(type)
#     return max_number
#
#
# print(get_max_number(1, int, 1, 2, 2, name='Vadym', book='Python'))

# x = 50
#
# def func(x):
#     print(f'x = {x}')
#     x = 2
#     print(f'We change x to {x}')
#     return x
#
#
# func(x)
# print(f'Finish x = {x}')

# x = 50
#
# def func():
#     global x
#     print(f'x = {x}')
#     x = 2
#     print(f'We change x to {x}')
#
# func()
# print(f'Finish x = {x}')


# def get_max_number(a: int, b: int) -> int:
#     if a > b:
#         return a
#     else:
#         return b
#
# print(get_max_number(1, 2))
# print(get_max_number(2.5, 2))


# def func(x):
#     def func_1(x):
#         print(f'Our x is {x}')
#     func_1(x)
#     return x * x
#
#
# print(func(5))

# f = lambda x: x * x
# print(f)
# print(f(5))
# sum_func = lambda x, y: x + y
# print(sum_func(3, 5))


# map and filter


# my_list_1 = [22, 54, 88]
# my_list_2 = [25, 33]
# my_list_3 = [25, 33]


# map(func, *iterables)

# def sum_two_number(x, y):
#     return x + y

# result = list(map(lambda x, y: x * y, my_list_1, my_list_2))

# print(result)

# filter
#
# result = list(filter(lambda x: x > 50, my_list_1))
#
# print(result)

#
# a = 1
#
# print(type(a))
#
# print(a is int)
#
# print(isinstance(a, float))
