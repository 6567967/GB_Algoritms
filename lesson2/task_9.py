# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing


def sum_digits(number: int) -> int:
    if number < 10:
        return number
    else:
        return number % 10 + sum_digits(number // 10)


max_number, cur_digits, number = 0, 0, 1

while number != 0:
    number = int(input("Введите натруальное число: "))
    if sum_digits(number) > cur_digits:
        max_number = number
        cur_digits = sum_digits(number)

if cur_digits == 0:
    print("Необходимо было ввести хотя бы одно натуральное число")
else:
    print(f"Максимальная сумма цифр {sum_digits(max_number)} у числа {max_number}")
