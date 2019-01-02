# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = 10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

spam_value = MIN_ITEM - 1
spam_index = -1

for index, item in enumerate(array):
    if spam_value < item < 0:
        spam_index = index
        spam_value = item
else:
    print(
        f"maximum negative {spam_value} at {spam_index} index"
        if spam_index != -1 else "no negative in array")
