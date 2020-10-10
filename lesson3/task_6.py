"""
6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.
"""
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

print(f"min-{spam_min}, max-{spam_max}")

eggs_sum = 0

for item in range(spam_min[0] + 1, spam_max[0]) \
        if spam_min[0] < spam_max[0] else \
        range(spam_max[0] + 1, spam_min[0]):
    eggs_sum += array[item]

print(eggs_sum)
