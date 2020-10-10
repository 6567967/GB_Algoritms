"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
кратны любому из чисел в диапазоне от 2 до 9.
"""

MIN_ITEM: int = 2
MAX_ITEM: int = 99
# array = [num for num in range(MIN_ITEM, MAX_ITEM + 1)]  # [2..MAX_ITEM]
array = list(range(MIN_ITEM, MAX_ITEM + 1))
# print(array)

value_count = {num: 0 for num in range(2, 9 + 1)}  # [2:0..9:0]
# print(value_count)

for item in array:
    for digit in value_count.keys():
        if item % digit == 0:
            value_count[digit] += 1

for item in value_count.items():
    print(*item, sep=' - ')
