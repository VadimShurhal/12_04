# (0°C × 9/5) + 32 = 32°F

# first_data = int(input('Enter first data '))
# second_data = int(input('Enter second data '))
#
# operation = input('Enter operation ')
#
# match operation:
#     case '+':
#         result = first_data + second_data
#         print('Result ', first_data + second_data)
#     case '-':
#         result = first_data - second_data
#         print('Result ', result)
#     case '*':
#         result = first_data * second_data
#         print('Result ', result)
#     case '/':
#         result = first_data / second_data
#         print('Result ', result)
#     case _:
#         print('Operator is not valid !')

# (0°C × 9/5) + 32 = 32°F
#
# celsius_temperature = int(input('Enter temperature :'))
#
# # kelvin_temperature = ((celsius_temperature * 9/5) + 32) if celsius_temperature > 0 else "Something wrong"
#
#
# if celsius_temperature > 0:
#     kelvin_temperature = ((celsius_temperature * 9/5) + 32)
# else:
#     kelvin_temperature = "Something wrong"
#
# print(kelvin_temperature)

# String

# a = ''
# b = ""
# c = """"""

"""
This
is a
comment
"""

# print(type(c))

# a = 'Hello'
# b = 'Ukraine'
#
# print(a+b)
# print(a*3)
#
#
# print("Hello", "Ukraine")

# a = 'Hello {} {} '
# print(a.format('Ukraine', 'Glory'))
#
# MY_CONSTANT = "kubectl get pods | grep {}"
#
# execute_command(MY_CONSTANT.format('pod_name'))

# f -string

# name = 'John'
# age = 18
#
# print(f'My name is {name} and my age {age}')


# a = 98 # --> int
# b = 2.2 # --> float
# c = True # --> Bool
#
# print(type(str(a)))
# print(type(str(b)))
# print(type(str(c)))
#
# age = 23
#
# print('My name is John ' + str(age) + " age old ")

# letters = 'HelloWorld'
# print(letters[2])
# print(letters[6])
# print(letters[-1])
# print(letters[-2])


# slice[start: end: step]

letters = 'Hello, and world, Ukraine, glory'

# a = letters[3:]
# print(a)
# b = letters[3:6]
# print(b)
# c = letters[::2]
# print(c)

# print(len(letters))

# print(letters.split(','))  ### --> list
#
# print(letters.title())
#
# print(letters.lower())
#
# print(letters.replace('and', 'or'))
#

# Type of string

# f"string"
# b"byte string"
# r"raw string"
#
# path = "It\"s \tstring\n yes "
#
# print(path)


# List


my_list = [1, 3, 4, 'string', 5.5, True]

# print(my_list)
#
# print(my_list[0])
#
# my_list[0] = 'New'
#
# print(my_list)

# print(len(my_list))
#
# my_string = 'hello'
# my_list = list(my_string)
# print(my_list)

# auto = ['BMW', 'Subaru', 'Audi']

# print('**** '.join(auto)) # list to string


# index_value = auto.index('audi')
# auto[index_value] = 'Audi auto'

# print(auto)
#
# print(auto.pop())
#
# print(auto)
#
# auto = ['BMW', 'Subaru', 'Audi', [1, 3, 55]]
#
# print(auto[3][2])
#
# auto.append(['Skoda', 'Alpha Romeo'])
#
# print(auto)
#
# print(auto[4][1])

# extend

# auto = ['Skoda', 'Alpha Romeo']
#
# auto_2 = ['BMW', 'Subaru', 'Audi']
#
# auto_2.extend(auto)
# print(auto_2)


auto = ['Skoda', 'Alpha Romeo']

# index_for_del = auto.index('Skoda')
#
# del auto[index_for_del]
# auto.remove('Skoda')

# print(auto)
#
# if 'Skosda' in auto:
#     print('Skoda is present')
#     auto.remove('Skoda')
# else:
#     pass
#

# tuple

my_tuple = (1, )
print(type(my_tuple))
# my_tuple = (1)  wrong
print(type(my_tuple))

my_tuple_2 = 1, 3, 4, 5
print(type(my_tuple_2))


a = tuple(auto)
print(a)

new_list = list(my_tuple_2)
print(new_list)
new_list.append('Audi')
print(tuple(new_list))


# tuple_list = tuple(new_list.append('Audi'))
# print(tuple_list)
# print(type(tuple_list))



################### ----->>>>>>>>>>>>>>>>>>>>>>>  *args and return
