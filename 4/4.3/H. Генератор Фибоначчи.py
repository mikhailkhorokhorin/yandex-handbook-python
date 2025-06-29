def fibonacci(num: int) -> int:
    value1, value2 = 0, 1
    for _ in range(num):
        yield value1
        value1, value2 = value2, value1 + value2