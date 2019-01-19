# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести
# число 6843.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

import cProfile

def reverse_recursive(number: int) -> int:
    if number > 9:
        return int(f"{number % 10}{reverse_recursive(number // 10)}")
    else:
        return number


# python3 -m timeit -n 100 -s "import task_1" "task_1.reverse_recursive(1)"
# 100 loops, best of 5: 105 nsec per loop - 1
# 100 loops, best of 5: 4.19 usec per loop - 10**10
# 100 loops, best of 5: 53.5 usec per loop - 10 ** 100
# 100 loops, best of 5: 129 usec per loop - 10 ** 200
# 100 loops, best of 5: 361 usec per loop - 10 ** 400
# 100 loops, best of 5: 1.16 msec per loop - 10**800
# cProfile.run('reverse_recursive(10**400)')
# 2/1    0.000    0.000    0.000    0.000 task_1.py:8(reverse_recursive) 10
# 11/1    0.000    0.000    0.000    0.000 task_1.py:8(reverse_recursive) 10**10
# 101/1    0.000    0.000    0.000    0.000 task_1.py:8(reverse_recursive) 10**100
# 401/1    0.000    0.000    0.000    0.000 task_1.py:8(reverse_recursive) 10**400
# 1 вызов на каждый знак. арифметика и ф-строки работают быстро. алгоритм
# ограничен стеком вызова. зависимость времени от числа знаков близка к линейной,
# но но чувствуется более выссокий порядок, который не может раскрыться из-за
# ограничений сетка вызова

def reverse_while(number: int) -> int:
    result = 0
    while number > 0:
        result = result * 10 + number % 10
        number = number // 10
    return result


# 100 loops, best of 5: 202 nsec per loop - 1
# 100 loops, best of 5: 1.12 usec per loop - 10 ** 10
# 100 loops, best of 5: 21.9 usec per loop - 10**100
# 100 loops, best of 5: 67.3 usec per loop - 10 ** 200
# 100 loops, best of 5: 228 usec per loop - 10**400
# 100 loops, best of 5: 821 usec per loop - 10**800
# 100 loops, best of 5: 1.27 msec per loop - 10**1000
# 100 loops, best of 5: 119 msec per loop - 10**10000
# cProfile.run('reverse_while(10**20000)')
# 1    0.033    0.033    0.033    0.033 task_1.py:28(reverse_while) 10**10000
# время линейно от количества входных данных. стек вызовов не наружается


def reverse_string_concat(number: int) -> int:
    result: str = ''
    num: str = str(number)
    for ch in num:
        result = ch + result
    return int(result)


# 100 loops, best of 5: 465 nsec per loop - 1
# 100 loops, best of 5: 1e+03 nsec per loop - 10**10
# 100 loops, best of 5: 6.33 usec per loop - 10**100
# 100 loops, best of 5: 12 usec per loop - 10**200
# 100 loops, best of 5: 26.1 usec per loop - 10**400
# 100 loops, best of 5: 61.3 usec per loop - 10**800
# 100 loops, best of 5: 83.1 usec per loop - 10**1000
# 100 loops, best of 5: 3.35 msec per loop - 10**10000
# 100 loops, best of 5: 12.3 msec per loop = 10**20000
# 100 loops, best of 5: 52.3 msec per loop - 10**40000
# cProfile.run('reverse_string_concat(10**10000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.004    0.004    0.004    0.004 task_1.py:53(reverse_string_concat)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# квадратично

def reverse_python_style(number: int) -> int:
    return int(str(number)[::-1])


# 100 loops, best of 5: 509 nsec per loop - 10**10
# 100 loops, best of 5: 1.51 usec per loop - 10**100
# 100 loops, best of 5: 20.1 usec per loop - 10**1000
# 100 loops, best of 5: 1.45 msec per loop - 10**10000
# 100 loops, best of 5: 5.6 msec per loop - 10**20000
# 100 loops, best of 5: 21.8 msec per loop - 10**40000
# cProfile.run('reverse_python_style(11**100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.006    0.006    0.193    0.193 <string>:1(<module>)
#         1    0.187    0.187    0.187    0.187 task_1.py:77(reverse_python_style)
#         1    0.000    0.000    0.193    0.193 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# квадратично, но быстрее предыдущего. самый быстрый метод из примененных

# рекурсия в данной задаче проигрывает из-за ограничения на длину входных данных
# реверс быстро делать отображением строки

def reverse_fstring(number: int) -> int:
    result: str = ''
    num: str = str(number)
    for ch in num:
        result = f"{ch}{result}"
    return int(result)

# 100 loops, best of 5: 3.48 msec per loop - 10**10000
# 100 loops, best of 5: 12.5 msec per loop - 10**20000
# 100 loops, best of 5: 52.8 msec per loop - 10**40000
# cProfile.run('reverse_fstring(11**100000)')
# calls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.006    0.006    0.404    0.404 <string>:1(<module>)
#         1    0.398    0.398    0.398    0.398 task_1.py:100(reverse_fstring)
#         1    0.000    0.000    0.404    0.404 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# разницу конкатенации c ф-строкой не увидел. не правильно использовал?


def test_reverse(func):
    assert func(0) == 0
    assert func(5) == 5
    assert func(32) == 23
    assert func(297) == 792
    assert func(1234567890) == 987654321
    assert func(int(10**100)) == 1
    print(f'test OK {func}')


# test_reverse(reverse_recursive)
# test_reverse(reverse_while)
# test_reverse(reverse_string_concat)
# print(reverse_string_concat(11**10000))
# print(reverse_string_concat(11**10000))
# test_reverse(reverse_python_style)
# test_reverse(reverse_fstring)
# print(10**10)
# print(10**20)
# print(10**40)


# import timeit
# print(timeit.timeit('int(str(10**40000)[::-1])', number=100))
