# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

assert SIZE > 1

spam_value = eggs_value = MAX_ITEM + 1
spam_index = eggs_index = -1

for index, item in enumerate(array):
    if (spam_value > item) & (eggs_index != index):
        spam_value = item
        spam_index = index
    if (eggs_value > array[-(index + 1)]) & (spam_index != SIZE - index - 1):
        eggs_value = array[-(index + 1)]
        eggs_index = SIZE - index - 1

print(spam_value, eggs_value)
