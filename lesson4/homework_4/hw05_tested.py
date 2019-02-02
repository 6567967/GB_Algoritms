# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import cProfile


def max_below_zero(size):
    # SIZE = 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
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


# "max_below_zero(10)"
# 1000 loops, best of 5: 13.2 usec per loop

# "max_below_zero(100)"
# 1000 loops, best of 5: 128 usec per loop

# "max_below_zero(1000)"
# 1000 loops, best of 5: 1.37 msec per loop

# "max_below_zero(10000)"
# 1000 loops, best of 5: 13.6 msec per loop


# cProfile.run('max_below_zero(10)')
#         56 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 tested.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 tested.py:8(max_below_zero)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('max_below_zero(100)')
#          508 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:218(randint)
#       100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 tested.py:10(<listcomp>)
#         1    0.000    0.000    0.000    0.000 tested.py:8(max_below_zero)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       103    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('max_below_zero(1000)')
#          5627 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.002    0.002 tested.py:10(<listcomp>)
#         1    0.000    0.000    0.002    0.002 tested.py:8(max_below_zero)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1622    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
