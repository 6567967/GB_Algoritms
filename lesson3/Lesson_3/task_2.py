import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 1000000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array.sort()    # прошу не использвать сортировки до урока 7
print(array)

find = int(input('Введите целое число для поиска: '))

# O(log n)
pos = len(array) // 2
left = 0
right = len(array) - 1
count = 1

while array[pos] != find and left <= right:
    count += 1
    if find > array[pos]:
        left = pos + 1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2

print('Элемент отсутствует' if left > right else f'Позиция элемента {pos}')
print(count)
