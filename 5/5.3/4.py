# Контроль параметров
def only_positive_even_sum(value1, value2) -> int:
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError
    elif not (value1 > 0 and not value1 % 2) or not (value2 > 0 and not value2 % 2):
        raise ValueError
    return value1 + value2
