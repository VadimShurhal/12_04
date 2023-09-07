import sys

a = []
b = a
b = b.append(1)
print(sys.getrefcount(a))
print(sys.getrefcount(b))
