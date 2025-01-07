# Классный прямоугольник
class Rectangle:
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float]) -> None:
        self.left_top_x = min(point1[0], point2[0])
        self.left_top_y = max(point1[1], point2[1])
        self.right_bottom_x = max(point1[0], point2[0])
        self.right_bottom_y = min(point1[1], point2[1])
        self.width = round(self.right_bottom_x - self.left_top_x, 2)
        self.height = round(self.left_top_y - self.right_bottom_y, 2)

    def perimeter(self) -> float:
        return round(2 * (self.width + self.height), 2)

    def area(self) -> float:
        return round(self.width * self.height, 2)
