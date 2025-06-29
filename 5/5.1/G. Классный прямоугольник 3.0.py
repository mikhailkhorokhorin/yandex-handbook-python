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

    def get_pos(self) -> tuple[float, float]:
        return round(self.left_top_x, 2), round(self.left_top_y, 2)

    def get_size(self) -> tuple[float, float]:
        return round(self.width, 2), round(self.height, 2)

    def move(self, dx: float, dy: float) -> None:
        self.__init__((self.left_top_x + dx, self.left_top_y + dy),
                      (self.right_bottom_x + dx, self.right_bottom_y + dy))

    def resize(self, width: float, height: float) -> None:
        self.__init__(self.get_pos(), (self.left_top_x + width, self.left_top_y - height))

    def turn(self) -> None:
        delta = (self.width - self.height) / 2
        self.__init__((self.left_top_x + delta, self.left_top_y + delta),
                      (self.right_bottom_x - delta, self.right_bottom_y - delta))

    def scale(self, factor: float) -> None:
        self.__init__(
                (self.left_top_x - self.width / 2 * (factor - 1),
                 self.left_top_y + self.height / 2 * (factor - 1)),
                (self.right_bottom_x + self.width / 2 * (factor - 1),
                 self.right_bottom_y - self.height / 2 * (factor - 1)))
