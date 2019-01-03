# 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.
# https://drive.google.com/file/d/1dRO7fXCLV1LLGWruoj_rnoHU5a8pRIjH/view?usp=sharing

n = int(input("Введите любое натуральное число: "))
left = 0

for i in range(n):
    left += (i+1)

right = (n*(n+1)) >> 1

print(f"1+2+...+n = n(n+1)/2 для n={n}:", end='')
if left == right:
    print("совпало")
else:
    print("не совпало o_O", left, right)
