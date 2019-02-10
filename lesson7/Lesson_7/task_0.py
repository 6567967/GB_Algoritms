import random

for arr_len in range(11):
    arr1 = [i for i in range(arr_len)]
    arr2 = arr1.copy()
    random.shuffle(arr2)
    accum = 1
    while  arr1 != arr2:
        random.shuffle(arr2)
        accum += 1
    print(f"{accum} random.shufle  {arr_len}")
