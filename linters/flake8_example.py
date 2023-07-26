from math import *
import itertools   # noqa:F401

def  CalculateSquareRoot (Number ):
	return  sqrt(Number )

def append_item(item, l=[]):
    l.append(item)
    return l

# f = lambda x: x * x
#
# print(f)


while True:
    try:
        your_number=float(input('Enter your number: '))
        print("Square root is:", CalculateSquareRoot(your_number))
        break
    except:  # noqa
        pass