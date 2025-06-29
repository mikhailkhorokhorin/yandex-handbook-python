class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c) -> tuple[float, float]:
    if sum(1 for i in (a, b, c) if isinstance(i, (int, float)) is True) != 3:
        raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError
    elif (a == b == 0 and c != 0) or b**2 < 4 * a * c:
        raise NoSolutionsError
    elif b**2 == 4 * a * c:
        return -b / (2 * a), -b / (2 * a)
    elif a == 0:
        return -c / b
    else:
        solutions = sorted(
            [
                (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a),
                (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a),
            ]
        )
        return solutions[0], solutions[1]
