# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите на
# экран исходный и отсортированный массивы.

import random

MIN_VALUE = 0
MAX_VALUE = 50
SIZE = 10


def rand_float(_min: float, _max: float) -> float:
    """ rand_float() -> x in the interval [min, max). """
    return random.random() * (_max - _min) + _min


def merge(arr1, arr2):
    assert len(arr1) > 0
    assert len(arr2) > 0
    result = list()
    first, second = 0, 0

    while first < len(arr1) and second < len(arr2):
        if arr1[first] <= arr2[second]:
            result.append(arr1[first])
            first += 1
        else:
            result.append((arr2[second]))
            second += 1
    result.extend(arr1[first:])
    result.extend(arr2[second:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    spam = merge(merge_sort(left), merge_sort(right))
    return spam


float_array = [rand_float(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(*float_array, 'v'*20, *merge_sort(float_array), sep='\n')


def test():
    for i in range(100000):
        arr1 = [rand_float(MIN_VALUE, MAX_VALUE) for _ in
                range(random.randint(0, 10))]
        arr2 = arr1.copy()
        arr1 = merge_sort(arr1)
        arr2.sort()
        assert arr1 == arr2
        print(f"Test {i} ok")

# test()
