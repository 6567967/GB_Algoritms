# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это
# цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’]
# и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
# from collections import namedtuple
from string import hexdigits
from string import digits
from collections import defaultdict


# def hex_str_to_list(string: str) -> list:
#     return list(string.upper())
#
# print(hex_str_to_list("a2"))
# print(hex_str_to_list("C4f"))

def hex_digit_to_int(char: str = 0) -> int:
    assert char in hexdigits
    return int(char) if char in digits else ord(char.upper()) - ord('A') + 10


hex_numbers = defaultdict(int)

for char in set(hexdigits.upper()):
    hex_numbers[char] = hex_digit_to_int(char)


# print(hex_numbers)


def int_to_hex(number: int) -> str:
    for hex_digit in hex_numbers:
        if hex_numbers[hex_digit] == number:
            return hex_digit


# print(int_to_hex(1))
# exit()

# print(tuple(map(lambda x: f"digit_{x}", set(hexdigits.upper()))))
#
# hex_digits = namedtuple('hex_digits', map(lambda x: f"digit_{x}", set(hexdigits.upper())))
# for char in set(hexdigits.upper()):
#     setattr(hex_digits, f"digit_{char}", hex_digit_to_int(char))
#     # hex_digits[char] = hex_digit_to_int(char)
#
# for key in hex_digits._fields():
#     print(hex_digits.key)
# exit()

# print(hex_digit_to_int("F"))
# exit()
# *****************************************************
number1 = deque(input("Введите первое hex: ").upper())
number2 = deque(input("Введите второе hex: ").upper())
# number1 = deque("a2")
# number2 = deque("c4f")
print(list(number1), list(number2), sep='\n')


# def hex_digit_to_int(char: str) -> int:
#     assert char not in [0-9]+['A'-'F']
#     return int(char) if char in [0-9] else ord(char)-ord('A')+10

# print(hex_digit_to_int("f"))

def hex_sum(number1: deque, number2: deque) -> deque:
    n1 = number1.copy()
    n2 = number2.copy()
    result = deque()
    overhead = False
    for i in range(max(len(n1), len(n2))):
        d1 = n1.pop() if len(n1) > 0 else '0'
        d2 = n2.pop() if len(n2) > 0 else '0'
        spam = hex_digit_to_int(d1) + hex_digit_to_int(d2)
        if overhead:
            spam += 1
        # print(d1, d2, hex_digit_to_int(d1), hex_digit_to_int(d2), spam, overhead)
        # print(spam % 16)
        overhead = spam // 16
        result.appendleft(int_to_hex(spam % 16))
    if overhead:
        result.appendleft('1')
    return result


print(f"{list(number1)}+{list(number2)}={list(hex_sum(number1, number2))}")


def hex_mull(n1: deque, n2: deque) -> deque:
    _num1 = n1.copy()
    _num1.reverse()
    _num2 = n2.copy()
    _num2.reverse()
    result = deque()
    for i in _num1:
        row = deque()
        overhead = 0
        for j in _num2:
            spam = hex_digit_to_int(i) * hex_digit_to_int(j)
            spam += overhead
            row.appendleft(int_to_hex(spam % 16))
            overhead = spam // 16
        if overhead > 0:
            row.appendleft(int_to_hex(overhead))
        result = hex_sum(result, row)
        _num2.appendleft('0')
    if result.count('0') == len(result):
        result = deque('0')
    return result


print(hex_mull(number1, number2))

# import random


# def test_sum():
#     for i in range(10000):
#         number1 = hex(random.randint(0, 1000))[2:]
#         number2 = hex(random.randint(0, 1000))[2:]
#         expect = deque(hex(int(number1, 16)+int(number2, 16))[2:].upper())
#         result = hex_sum(deque(str(number1)), deque(str(number2)))
#         assert expect == result
#
#         print(f"sum {i} ok ", end = '')
#         print(f"{number1}+{number2}=",*expect, '/', *result, sep='')
#
#
# test_sum()
#
#
# def test_mul():
#     for i in range(100000):
#         number1 = hex(random.randint(0, 100000))[2:]
#         number2 = hex(random.randint(0, 100000))[2:]
#         expect = deque(hex(int(number1, 16)*int(number2, 16))[2:].upper())
#         result = hex_mull(deque(str(number1)), deque(str(number2)))
#         assert expect == result, f"{number1}*{number2}={expect},{result}"
#         print(f"mul {i} ok ", end = '')
#         print(f"{number1}*{number2}=", *expect, '/', *result, sep='')
#
#
# test_mul()
