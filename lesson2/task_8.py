# 8. Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

num_count = int(input("Введите количество чисел: "))
digit = int(input("Введите искому цифру: "))

digit_count = 0

for i in range(num_count):
    number = int(input(f"Введите {i+1}-ое натуральное число: "))  # или нулевые числа надо считать дополнительно
    while number != 0:
        if number % 10 == digit:
            digit_count += 1
        number = number // 10

print(f"Цифра {digit} встретилась {digit_count} раз")
