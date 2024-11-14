def merge(a1: tuple, a2: tuple) -> tuple:
    a = list(a1) + list(a2)
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return tuple(a)
