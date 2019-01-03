# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1c86G8R4h6oDPV0pXFxPxQY8CKDrhjNGV/view?usp=sharing

print("Введите трёхзначное число")
number = int(input("number="))

h = number // 100
d = number // 10 % 10
n = number % 10
sum_of_digits = h + d + n
multiply = h * d * n

print(f"Сумма {h}+{d}+{n}={sum_of_digits}, а произведение {h}*{d}*{n}={multiply}")
