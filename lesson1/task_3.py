# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print("Введите координаты точек прямой:")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

A = y1 - y2
B = x2 - x1
C = x1 * y2 - x2 * y1

print(f"Уравнение прямой, проходящей через точки ({x1},{y1}), ({x2},{y2})\n \
    имеет вид {A}x+{B}y+{C}=0")