# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
# массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если
# индексация начинается с нуля), т.к. именно в этих позициях первого массива
# стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# even_indexes = set()  #indexes unique
#
# for index, item in enumerate(array):
#     if item % 2 == 0:
#         even_indexes.add(index)
# print(even_indexes)
#
# even_indexes_list = list(even_indexes)
# print(even_indexes.__sizeof__(), even_indexes_list.__sizeof__())  # huge


even_indexes = list()
for index, item in enumerate(array):
    if item % 2 == 0:
        even_indexes.append(index)
print(even_indexes)
