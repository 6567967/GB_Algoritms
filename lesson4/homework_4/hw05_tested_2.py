# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def max_below_zero(array):
    # SIZE = 10
    # print(array)

    i = 0
    index = -1

    while i < size:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

        i += 1

    # print(f'Число {array[index]} на позиции {index}')
    return f'Число {array[index]} на позиции {index}'


size = 1000
array = [random.randint(size * -10, size * 10) for _ in range(size)]

# python -m timeit -n 100 -s "import hw05_tested_2" "hw05_tested_2.max_below_zero(hw05_tested_2.array)"
# 100 loops, best of 3: 1.66 usec per loop    - 10
# 100 loops, best of 3: 12.7 usec per loop    - 100
# 100 loops, best of 3: 140 usec per loop     - 1000
# 100 loops, best of 3: 1.39 msec per loop    - 10000

cProfile.run('max_below_zero(array)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 hw05_tested_2.py:8(max_below_zero)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
