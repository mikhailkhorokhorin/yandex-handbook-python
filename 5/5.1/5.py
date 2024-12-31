class Rectangle:
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float]) -> None:
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def perimeter(self) -> float:
        return round(2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1)), 2)

    def area(self) -> float:
        return round(abs(self.x2 - self.x1) * abs(self.y2 - self.y1), 2)
