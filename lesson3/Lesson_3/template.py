import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(*array)

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
          for _ in range(SIZE)]

