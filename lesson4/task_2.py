# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и
# сложность алгоритмов. Результаты анализа сохранить в виде комментариев
# в файле с кодом.

import cProfile


def sieve(number: int) -> int:
    numbers: list = [i for i in range((number + 1) * (number + 1))]
    numbers[1] = 0
    for i in range(2, len(numbers)):
        if numbers[i] != 0:
            j = i + i
            while j < len(numbers):
                numbers[j] = 0
                j += i
    result = [i for i in numbers if i != 0]
    return result[number - 1]


def sieve_len(number: int) -> int:
    numbers: list = [i for i in range((number + 1) * (number + 1))]
    numbers[1] = 0
    length_numbers = len(numbers)
    for i in range(2, length_numbers):
        if numbers[i] != 0:
            j = i + i
            while j < length_numbers:
                numbers[j] = 0
                j += i
    result = [i for i in numbers if i != 0]
    return result[number - 1]


def not_sieve1(number: int) -> int:
    numbers = list()
    k = 0
    for i in range(2, (number + 1) ** 2):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            numbers.append(i)
        else:
            k = 0
    return numbers[number - 1]


def not_sieve2(number: int) -> int:
    numbers = [2]
    for i in range(3, (number + 1) ** 2, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in numbers:
            if j * j - 1 > i:
                numbers.append(i)
                break
            if (i % j == 0):
                break
        else:
            numbers.append(i)
        if len(numbers) >= number:
            break
    return numbers[number - 1]


def test_simple(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i} OK')


# test_simple(not_sieve1)
# test_simple(not_sieve2)

# print(sieve(10000))
# test_simple(sieve)
# test_simple(not_sieve)

# python3 -m timeit -n 100 -s "import task_2" "task_2.sieve(1)"
# 100 loops, best of 5: 1.57 usec per loop - 1
# 100 loops, best of 5: 29.8 usec per loop - 10
# 100 loops, best of 5: 3.88 msec per loop - 100
# 100 loops, best of 5: 522 msec per loop - 1000
pass
# cProfile.run('sieve(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.007    0.007    0.720    0.720 <string>:1(<module>)
#       1    0.524    0.524    0.712    0.712 task_2.py:10(sieve)
#       1    0.033    0.033    0.033    0.033 task_2.py:11(<listcomp>)
#       1    0.027    0.027    0.027    0.027 task_2.py:19(<listcomp>)
#       1    0.000    0.000    0.720    0.720 {built-in method builtins.exec}
# 2859565    0.128    0.000    0.128    0.000 {built-in method builtins.len}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# упс. надо завести переменную )
# cProfile.run('sieve_len(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.007    0.007    0.355    0.355 <string>:1(<module>)
# 1    0.289    0.289    0.348    0.348 task_2.py:23(sieve_len)
# 1    0.033    0.033    0.033    0.033 task_2.py:24(<listcomp>)
# 1    0.027    0.027    0.027    0.027 task_2.py:33(<listcomp>)
# 1    0.000    0.000    0.355    0.355 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# python3 -m timeit -n 100 -s "import task_2" "task_2.sieve_len(100)"
# 100 loops, best of 5: 2.61 msec per loop - 100
# чутка полегчало )
pass
# python3 -m timeit -n 100 -s "import task_2" "task_2.not_sieve1(1)"
# 100 loops, best of 5: 1.19 usec per loop 1
# 100 loops, best of 5: 284 usec per loop 10
# для 100 не дождался
# очень долго. надо оптимизировать )
# cProfile.run('not_sieve1(100)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    2.861    2.861 <string>:1(<module>)
#    1    2.860    2.860    2.861    2.861 task_2.py:38(not_sieve1)
#    1    0.000    0.000    2.861    2.861 {built-in method builtins.exec}
# 1252    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# python3 -m timeit -n 100 -s "import task_2" "task_2.not_sieve2(1)"
# 100 loops, best of 5: 917 nsec per loop - 1
# 100 loops, best of 5: 5.29 usec per loop - 10
# 100 loops, best of 5: 124 usec per loop - 100
# 100 loops, best of 5: 3.15 msec per loop - 1000
# 100 loops, best of 5: 74.7 msec per loop - 10000
# терпимо, можно в продакшн )
# cProfile.run('not_sieve2(1000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#    1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#    1    0.003    0.003    0.004    0.004 task_2.py:51(not_sieve2)
#    1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
# 3168    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#  999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# хотя надо бы добавить расчет длины масива, возможно уменьшив количество вызовов
# len увеличится скорость
# но моё время на ДЗ вышло, поэтому сдаю что есть
