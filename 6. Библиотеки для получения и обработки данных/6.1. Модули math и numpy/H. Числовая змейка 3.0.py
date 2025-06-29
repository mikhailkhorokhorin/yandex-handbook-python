import numpy as np


def snake(m: int, n: int, direction: str = "H") -> np.array:
    matrix, num = np.zeros((n, m), dtype="int16"), 1
    for i in range(n if direction == "H" else m):
        if direction == "H":
            matrix[i] = (
                np.arange(num, num + m)
                if i % 2 == 0
                else np.arange(num + m - 1, num - 1, -1)
            )
        else:
            matrix[:, i] = (
                np.arange(num, num + n)
                if i % 2 == 0
                else np.arange(num + n - 1, num - 1, -1)
            )
        num += m if direction == "H" else n
    return matrix
