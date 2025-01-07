# Рекурсивный сумматор
def recursive_sum(*args) -> int:
    return 0 if not args else args[0] + recursive_sum(*args[1:])
