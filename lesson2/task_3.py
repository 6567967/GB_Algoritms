# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing


def reverse(number: int) -> int:
    if number > 9:
        return int(f"{number % 10}{reverse(number // 10)}")
    else:
        return number


print(f"обратное - {(reverse(int(input('Введите число: '))))}")
