# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

number = int(input("Введите натурально число: "))

odd, even = 0, 0

while number > 0:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
    number = number // 10

print(f"{odd} - нечетных, {even} - четных")
