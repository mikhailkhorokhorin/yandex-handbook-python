def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

