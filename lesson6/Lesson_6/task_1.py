import sys
import gc

a = [1, 2, 3]
a.append(a)
print(a)
b = a
del a
del b
# print(sys.getrefcount(b))
print('hello')

