def func(a, b):
    """
    func(2, 5)
    '2, 3, 4, 5'
    """
    if a == b:
        return f'{a}'

    if a < b:
        return f'{a}, {func(a + 1, b)}'

    if a > b:
        return f'{a}, {func(a - 1, b)}'


print(func(20, 5))
