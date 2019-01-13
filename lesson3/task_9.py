# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
          for _ in range(SIZE)]
print(*matrix, sep='\n')

min_values = [MAX_ITEM + 1 for _ in range(SIZE)]
max_value = MIN_ITEM - 1

for col in range(SIZE):
    for row in range(SIZE):
        if min_values[col] > matrix[row][col]:
            min_values[col] = matrix[row][col]
    if max_value < min_values[col]:
        max_value = min_values[col]

print('*' * SIZE * 4)
print(f"minimum in columns: \n{min_values}")
print(f"maximum from them: {max_value}")
