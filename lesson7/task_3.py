# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
# его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки
# исходного массива. Но если это слишком сложно, то используйте метод
# сортировки, который не рассматривался на уроках

import random

M = 5
MIN_VALUE = 0
MAX_VALUE = 100

# [MIN_VALUE, MAX_VALUE)
int_array = [random.randrange(MIN_VALUE, MAX_VALUE) for _ in range(M * 2 + 1)]
print(int_array)


def get_median(arr) -> int:
    assert len(arr) % 2 == 1
    return hoar_select(arr, len(arr) // 2)


def hoar_select(arr, index: int) -> int:
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    equal = [item for item in arr if item == pivot]
    less = [item for item in arr if item < pivot]
    greater = [item for item in arr if item > pivot]
    # print(less, greater, equal, index)

    if index < len(less):
        return hoar_select(less, index)
    elif index < len(equal) + len(less):
        return equal[0]
    else:
        return hoar_select(greater, index - len(less) - len(equal))


print(get_median(int_array))


def test():
    assert get_median([42]) == 42
    assert get_median([1, 2, 3]) == 2

    import statistics
    for i in range(100000):
        tmp_array = [random.randrange(MIN_VALUE, MAX_VALUE) for _ in
                     range(random.randrange(0, M) * 2 + 1)]
        assert get_median(tmp_array) == statistics.median(tmp_array)
        print(f"test {i} ok", tmp_array)


# test()
