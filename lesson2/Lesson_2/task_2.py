import sys

sys.setrecursionlimit(1500)


def akk(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return akk(m - 1, 1)
    return akk(m - 1, akk(m, n - 1))


print(akk(3, 9))
