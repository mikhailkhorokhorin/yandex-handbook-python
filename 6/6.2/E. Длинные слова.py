from pandas import Series


def get_long(data: Series, min_length: int = 5) -> Series:
    return data[data >= min_length]
