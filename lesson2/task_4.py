# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing


def sum_row(n: int) -> float:
    if n == 0:
        return 0
    else:
        return 1 - sum_row(n-1)*0.5


print(f"равна {sum_row(int(input('Сумма элементов ряда(1 -0.5 0.25 -0.125 ...) в количестве: ')))}")
