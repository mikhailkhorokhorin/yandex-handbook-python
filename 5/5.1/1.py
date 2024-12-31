from math import sqrt


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def length(self, point) -> int:
        return round(sqrt(pow(point.x - self.x, 2) + pow(point.y - self.y, 2)), 2)
