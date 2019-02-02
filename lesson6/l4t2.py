# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и
# сложность алгоритмов. Результаты анализа сохранить в виде комментариев
# в файле с кодом.

import cProfile
import memory_profiler


# python3 -m memory_profiler l4t2
@memory_profiler.profile
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


@memory_profiler.profile
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


@memory_profiler.profile
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


@memory_profiler.profile
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


@memory_profiler.profile
def test_simple(func):
    lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {i} OK')


sieve(50)
sieve_len(80)
not_sieve1(20)
not_sieve2(400)

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     12     14.3 MiB     14.3 MiB   @memory_profiler.profile
#     13                             def sieve(number: int) -> int:
#     14     14.6 MiB      0.3 MiB       numbers: list = [i for i in range((number + 1) * (number + 1))]
#     15     14.6 MiB      0.0 MiB       numbers[1] = 0
#     16     14.6 MiB      0.0 MiB       for i in range(2, len(numbers)):
#     17     14.6 MiB      0.0 MiB           if numbers[i] != 0:
#     18     14.6 MiB      0.0 MiB               j = i + i
#     19     14.6 MiB      0.0 MiB               while j < len(numbers):
#     20     14.6 MiB      0.0 MiB                   numbers[j] = 0
#     21     14.6 MiB      0.0 MiB                   j += i
#     22     14.6 MiB      0.0 MiB       result = [i for i in numbers if i != 0]
#     23     14.6 MiB      0.0 MiB       return result[number - 1]
#
#
# Filename: /home/ifl/Documents/Алгоритмы и структуры данных на Python/lessons/lesson6/l4t2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     26     14.6 MiB     14.6 MiB   @memory_profiler.profile
#     27                             def sieve_len(number: int) -> int:
#     28     14.7 MiB      0.1 MiB       numbers: list = [i for i in range((number + 1) * (number + 1))]
#     29     14.7 MiB      0.0 MiB       numbers[1] = 0
#     30     14.7 MiB      0.0 MiB       length_numbers = len(numbers)
#     31     14.7 MiB      0.0 MiB       for i in range(2, length_numbers):
#     32     14.7 MiB      0.0 MiB           if numbers[i] != 0:
#     33     14.7 MiB      0.0 MiB               j = i + i
#     34     14.7 MiB      0.0 MiB               while j < length_numbers:
#     35     14.7 MiB      0.0 MiB                   numbers[j] = 0
#     36     14.7 MiB      0.0 MiB                   j += i
#     37     14.7 MiB      0.0 MiB       result = [i for i in numbers if i != 0]
#     38     14.7 MiB      0.0 MiB       return result[number - 1]
#
#
# Filename: /home/ifl/Documents/Алгоритмы и структуры данных на Python/lessons/lesson6/l4t2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     41     14.7 MiB     14.7 MiB   @memory_profiler.profile
#     42                             def not_sieve1(number: int) -> int:
#     43     14.7 MiB      0.0 MiB       numbers = list()
#     44     14.7 MiB      0.0 MiB       k = 0
#     45     14.7 MiB      0.0 MiB       for i in range(2, (number + 1) ** 2):
#     46     14.7 MiB      0.0 MiB           for j in range(2, i):
#     47     14.7 MiB      0.0 MiB               if i % j == 0:
#     48     14.7 MiB      0.0 MiB                   k = k + 1
#     49     14.7 MiB      0.0 MiB           if k == 0:
#     50     14.7 MiB      0.0 MiB               numbers.append(i)
#     51                                     else:
#     52     14.7 MiB      0.0 MiB               k = 0
#     53     14.7 MiB      0.0 MiB       return numbers[number - 1]
#
#
# Filename: /home/ifl/Documents/Алгоритмы и структуры данных на Python/lessons/lesson6/l4t2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     56     14.7 MiB     14.7 MiB   @memory_profiler.profile
#     57                             def not_sieve2(number: int) -> int:
#     58     14.7 MiB      0.0 MiB       numbers = [2]
#     59     14.7 MiB      0.0 MiB       for i in range(3, (number + 1) ** 2, 2):
#     60     14.7 MiB      0.0 MiB           if (i > 10) and (i % 10 == 5):
#     61     14.7 MiB      0.0 MiB               continue
#     62     14.7 MiB      0.0 MiB           for j in numbers:
#     63     14.7 MiB      0.0 MiB               if j * j - 1 > i:
#     64     14.7 MiB      0.0 MiB                   numbers.append(i)
#     65     14.7 MiB      0.0 MiB                   break
#     66     14.7 MiB      0.0 MiB               if (i % j == 0):
#     67     14.7 MiB      0.0 MiB                   break
#     68                                     else:
#     69     14.7 MiB      0.0 MiB               numbers.append(i)
#     70     14.7 MiB      0.0 MiB           if len(numbers) >= number:
#     71     14.7 MiB      0.0 MiB               break
#     72     14.7 MiB      0.0 MiB       return numbers[number - 1]
#
#
# (var: cProfile) 	 (type: module) 	 (full size: 80)
# (var: memory_profiler) 	 (type: module) 	 (full size: 80)
# <function not_sieve1 at 0x7f2993312378> can hide some variables, try memory_profile
# (var: not_sieve1) 	 (type: function) 	 (full size: 136)
# <function not_sieve2 at 0x7f2993312268> can hide some variables, try memory_profile
# (var: not_sieve2) 	 (type: function) 	 (full size: 136)
# <function sieve at 0x7f29933127b8> can hide some variables, try memory_profile
# (var: sieve) 	 (type: function) 	 (full size: 136)
# <function sieve_len at 0x7f2993312510> can hide some variables, try memory_profile
# (var: sieve_len) 	 (type: function) 	 (full size: 136)
# <function test_simple at 0x7f2993312158> can hide some variables, try memory_profile
# (var: test_simple) 	 (type: function) 	 (full size: 136)
# total size: 840
