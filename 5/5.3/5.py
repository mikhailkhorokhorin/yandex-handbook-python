# Слияние с проверкой
def merge(value1, value2):
    if not hasattr(value1, "__iter__") or not hasattr(value2, "__iter__"):
        raise StopIteration
    if not all(isinstance(x, type(value1[0])) for x in (list(value1) + list(value2))):
        raise TypeError
    if list(value1) != sorted(value1) or list(value2) != sorted(value2):
        raise ValueError
    return tuple(sorted(list(value1) + list(value2)))
