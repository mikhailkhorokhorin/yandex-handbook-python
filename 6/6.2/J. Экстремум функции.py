from numpy import arange
from pandas import Series


def values(func, start: float, end: float, step: float) -> Series:
    index = arange(start, end + step, step)
    return Series(map(func, index), index=index, dtype="float64")


def min_extremum(data: Series) -> float:
    return min(data[data == min(data)].index)


def max_extremum(data: Series) -> float:
    return max(data[data == max(data)].index)
