# 3. В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

spam_min = [-1, MAX_ITEM + 1]
spam_max = [-1, MIN_ITEM - 1]

for index, item in enumerate(array):
    if spam_min[1] > item:
        spam_min[0] = index
        spam_min[1] = item
    if spam_max[1] < item:
        spam_max = [index, item]
else:
    array[spam_max[0]], array[spam_min[0]] = \
        array[spam_min[0]], array[spam_max[0]]

print(array)
