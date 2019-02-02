# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

MIN_VALUE = -100
MAX_VALUE = 99
SIZE = 25

int_array = [randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
print(*int_array)


def bubble_sort_reverse(array):
    n = 1
    while n < len(array):
        swap = False  # no exchanges in inner cycle?
        for i in range(len(array) - n):  # items n+ already sorted
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True  # sorting in progress
        if not swap:
            break  # already sorted
        n += 1


bubble_sort_reverse(int_array)
print(*int_array)


def test():
    for i in range(1000):
        arr1 = [randint(MIN_VALUE, MAX_VALUE) for _ in range(SIZE)]
        arr2 = arr1.copy()
        bubble_sort_reverse(arr1)
        arr2.sort(reverse=True)
        assert arr1 == arr2
        print(f"Test {i} ok")

# test()
