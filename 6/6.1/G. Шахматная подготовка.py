import numpy as np


def make_board(number: int) -> np.array:
    return np.array(
        np.rot90(np.indices((number, number)).sum(axis=0) % 2), dtype="int8"
    )
