# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

i = 0
index = -1

while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i

    i += 1

print(f'Число {array[index]} на позиции {index}')
