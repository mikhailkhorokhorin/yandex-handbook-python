def fibonacci(num: int) -> int:
    val1, val2 = 0, 1
    for _ in range(num):
        yield val1
        val1, val2 = val2, val1 + val2

