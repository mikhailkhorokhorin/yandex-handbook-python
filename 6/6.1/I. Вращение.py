import numpy as np


def rotate(matrix: np.array, angle: int) -> np.array:
    return np.rot90(matrix, (360 - angle) // 90)
