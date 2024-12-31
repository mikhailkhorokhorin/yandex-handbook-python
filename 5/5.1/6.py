class Rectangle:
    def __init__(self, point1: tuple[float, float], point2: tuple[float, float]) -> None:
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2
        self.width, self.height = round(abs(self.x2 - self.x1), 2), round(abs(self.y2 - self.y1), 2)

    def perimeter(self) -> float:
        return round(2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1)), 2)

    def area(self) -> float:
        return round(abs(self.x2 - self.x1) * abs(self.y2 - self.y1), 2)

    def get_pos(self) -> tuple[float, float]:
        return round(min(self.x1, self.x2), 2), round(max(self.y1, self.y2), 2)

    def get_size(self) -> tuple[float, float]:
        return self.width, self.height

    def move(self, dx: float, dy: float) -> None:
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
        self.__init__((self.x1, self.y1), (self.x2, self.y2))

    def resize(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
