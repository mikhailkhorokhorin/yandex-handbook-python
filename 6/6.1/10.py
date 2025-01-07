# Лесенка
import numpy as np


def stairs(vector: np.array) -> np.array:
    return np.array([np.roll(vector, i) for i in range(len(vector))])
