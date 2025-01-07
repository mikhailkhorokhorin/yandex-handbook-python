# Слияние
def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    both = list(tuple1) + list(tuple2)
    for i in range(len(both)):
        for j in range(0, len(both) - i - 1):
            if both[j] > both[j + 1]:
                both[j], both[j + 1] = both[j + 1], both[j]
    return tuple(both)
