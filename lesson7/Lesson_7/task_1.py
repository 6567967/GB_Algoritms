array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]

def bubble_sort(array):
    n = 1
    while n < len(array):
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        if not swap:
            break
        n += 1


bubble_sort(array)
print(array)
