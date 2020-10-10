"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
элементов строк. Программа должна вычислять сумму введенных элементов
каждой строки и записывать ее в последнюю ячейку строки. В конце следует
вывести полученную матрицу.
"""

import random

ROWS = 5
COLUMNS = 4
SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 100

matrix = [[0 for _ in range(COLUMNS)]
          for _ in range(ROWS)]

sample_numbers: str = ' '.join(
    [str(random.randint(MIN_ITEM, MAX_ITEM)) for _ in range(SIZE)])

for index, item in enumerate(map(int, input(f"input 3*5 numbers"
                                            f"(ex. {sample_numbers}):").split())):
    matrix[index // 3][index % 3] = item
    matrix[index // 3][3] += item
print(*matrix, sep='\n')
