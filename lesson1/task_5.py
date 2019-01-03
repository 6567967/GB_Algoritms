# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
# и сколько между ними находится букв.

print("Введите две строчных латинских буквы")
first = input("Первая буква: ")
second = input("Вторая буква: ")

if first == second:
    n = ord(first) - ord('a') + 1
    print(f"Введены одинаковые {n}-е буквы {first}")
else:
    n1 = ord(first) - ord('a') + 1
    n2 = ord(second) - ord('a') + 1
    offset = abs(n1 - n2) - 1
    print(f"Между {n1}-й буквой {first} и {n2}-й буквой {second} {offset} букв(а/ы)")
