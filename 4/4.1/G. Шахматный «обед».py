def can_eat(knight: tuple[int, int], other: tuple[int, int]) -> bool:
    return abs(knight[0] - other[0]) + abs(knight[1] - other[1]) == 3
