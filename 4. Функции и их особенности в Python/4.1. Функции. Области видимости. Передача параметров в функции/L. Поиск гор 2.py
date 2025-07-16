from itertools import product


def find_mountains(heights: list[list[int]]) -> tuple[tuple[int, int], ...]:
    n = len(heights)
    m = len(heights[0])
    result = []
    for i, j in product(range(1, n - 1), range(1, m - 1)):
        if all(
            heights[i][j] > heights[k][t]
            for k, t in product(range(i - 1, i + 2), range(j - 1, j + 2))
            if (k, t) != (i, j)
        ):
            result.append((i + 1, j + 1))

    return tuple(result)
