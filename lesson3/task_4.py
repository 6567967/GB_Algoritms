"""
4. Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num_freq = dict()
most_wanted = [-1, MIN_ITEM - 1]

for item in array:
    if num_freq.get(item) is None:
        num_freq[item] = 1
    else:
        num_freq[item] += 1

    if most_wanted[0] < num_freq[item]:
        most_wanted = [num_freq[item], item]

print(f"{most_wanted[1]}({most_wanted[0]}-times)"
      if most_wanted[0] != -1 else "no item in array")
