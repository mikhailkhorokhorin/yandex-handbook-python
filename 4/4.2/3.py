def NOD(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd(*args) -> int:
    a = list(args)
    res = 0
    for i in range(len(a)):
        res = NOD(res, a[i])
    return res
