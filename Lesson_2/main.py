# -->> int()

# snake_case

first_variable = 1


def first_method():
    pass


# CamelCase


class MeClassFirst:
    pass


#SCREAMING_SNAKE_CASE


SCREAMING_SNAKE_CASE = '192.68.0.2'
# This IP use for our stage

# --------------------------------------------------------


# Boolean Type

# True
# False

# print(1 == 1)
#
# print(1 == 2)
#
# # --------------------------------------------------------
#
#
# print(132132131321)
# print(132121)
#
# # --------------------------------------------------------
#
# print(23.1)
#
#
# print(type(132132131321))
# print(type(23.1))
# print(type([1, '32', 3]))
# print(type((1, 2, 3, 3)))
# print(type('Hello'))
# print(type({(1, 2, 3, 3)}))
# # this is dict
# print({'name': 'Vadym', 'age': 30})

# Ctrl + /

# --------------------------------------------------------

# print(1+1)
# print(1-1)
# print(4*12)
# print(36/10)
#
# print(36%10)
# print(36//10)
#
# # --------------------------------------------------------
#
# print(3>2)
# print(3<2)
# print(3==2)
# print(3!=2)
#
# print(2>=2)
# print(3<=2)


# --------------------------------------------------------

# is
# is not

# a = [1]  # list()
# b = [1]  # list()
#
#
# print(a == b)
#
# print(type(a))
# print(type(b))
#
#
# print(id(a))
# print(id(b))
#
# print(a is not b)

# print(None is None)

# in and not

# my_list = [1, 2, 3, 4]
#
# print(22 not in my_list)

# print(*objects, sep=' ', end='\n', file=None, flush=False)¶
# *args

# print('Hello Ukraine', sep='\n', end='!!!!')

# *args = 'Hello Ukraine', 'Glory', '2023', 22, [1,2], {1 : 'O'}




# int_variable = 11
#
# my_string = str(int_variable)
#
# print(my_string)
#
# print(type(my_string))


# age = input('Set age :')
#
# print(type(age))
# print(age)

# if
# elif
# else

my_variable_1 = int(input('Set first variable : '))
my_variable_2 = int(input('Set second variable : '))

if my_variable_1 > my_variable_2:
    print('First variable more than second')
elif my_variable_1 == my_variable_2:   # else if
    print('variable is equal')
else:
    print('Second variable more than first')

