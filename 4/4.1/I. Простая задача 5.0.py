def is_prime(num: int) -> bool:
    return sorted({i for d in range(2, int(num ** 0.5) + 1) if num % d == 0 for i in (d, num // d)}) == []
