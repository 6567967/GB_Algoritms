# Начало
# Вывод("Введите два числа")
# Ввод(Первое число)
# Ввод(Второе число)
# Если Второе число != 0
# то частное = первое число / второе число
#     Вывод("Результат равен", частное)
# иначе Вывод("Нет решения")
# Конец

print('Введите два числа')
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))

if b != 0:
    c = a / b
    print(f'Результат равен {c}')
else:
    print('Нет решения')