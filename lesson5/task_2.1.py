# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это
# цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from string import hexdigits
from string import digits
import cProfile


def hex_digit_to_int(char: str = '0') -> int:
    assert char in hexdigits, f'{char} not a hex digit'
    return int(char) if char in digits else ord(char.upper()) - ord('A') + 10

hex_numbers = list(hexdigits.upper())[:16]


def int_to_hex(number: int) -> str:
    return hex_numbers[number]


number1 = list(input("Введите первое hex: ").upper())
number2 = list(input("Введите второе hex: ").upper())
# number1 = list("a2".upper())
# number2 = list("c4f".upper())
print(number1, number2, sep='\n')


def hex_sum(num1: list, num2: list) -> list:
    n1 = num1.copy()
    n2 = num2.copy()
    result = deque()
    overhead = False
    for i in range(max(len(n1), len(n2))):
        d1 = n1.pop() if len(n1) > 0 else '0'
        d2 = n2.pop() if len(n2) > 0 else '0'
        spam = hex_digit_to_int(d1) + hex_digit_to_int(d2)
        if overhead:
            spam += 1
        overhead = spam // 16
        result.appendleft(int_to_hex(spam % 16))
    if overhead:
        result.appendleft('1')
    return list(result)

# cProfile.run('hex_sum(["a"]*10000, ["b"]*10000)')
# exit()
print(f"{list(number1)}+{list(number2)}={list(hex_sum(number1, number2))}")
print(*number1, '+', *number2,'=', *hex_sum(number1, number2), sep='')


def hex_mull(n1: list, n2: deque) -> deque:
    _num1 = n1.copy()
    _num2 = deque(n2.copy())
    _num2.reverse()
    result = deque()
    for i in _num1[::-1]:
        row = deque()
        overhead = 0
        for j in _num2:
            spam = hex_digit_to_int(i) * hex_digit_to_int(j)
            spam += overhead
            row.appendleft(int_to_hex(spam % 16))
            overhead = spam // 16
        if overhead > 0:
            row.appendleft(int_to_hex(overhead))
        result = hex_sum(list(result), list(row))
        _num2.appendleft('0')
    if result.count('0') == len(result):
        result = deque('0')
    return result


print(hex_mull(number1, deque(number2)))
print(*number1, '*', *number2,'=', *hex_mull(number1, deque(number2)), sep='')


# import random
#
#
# def test_sum():
#     for i in range(10000):
#         number1 = hex(random.randint(0, 1000))[2:]
#         number2 = hex(random.randint(0, 1000))[2:]
#         expect = list(hex(int(number1, 16) + int(number2, 16))[2:].upper())
#         result = hex_sum(list(str(number1)), list(str(number2)))
#         assert expect == result, f"{number1}+{number2}={expect},{result}"
#         print(f"sum {i} ok ", end='')
#         print(f"{number1}+{number2}=", *expect, '/', *result, sep='')
#
#
# test_sum()
#
#
# def test_mul():
#     for i in range(10000):
#         number1 = hex(random.randint(0, 100000))[2:]
#         number2 = hex(random.randint(0, 100000))[2:]
#         expect = list(hex(int(number1, 16) * int(number2, 16))[2:].upper())
#         result = hex_mull(list(str(number1)), deque(str(number2)))
#         assert expect == result, f"{number1}*{number2}={expect},{result}"
#         print(f"mul {i} ok ", end='')
#         print(f"{number1}*{number2}=", *expect, '/', *result, sep='')
#
#
# test_mul()
