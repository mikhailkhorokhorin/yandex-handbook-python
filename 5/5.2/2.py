# Классная точка 4.0
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def length(self, point) -> int:
        return round((((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args) -> None:
        if not args:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        else:
            self.x, self.y = args

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"PatchedPoint({self.x}, {self.y})"