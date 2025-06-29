# 5.1. Объектная модель Python. Классы, поля и методы
### A. Классная точка
```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
```
### B. Классная точка 2.0
```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def length(self, point) -> int:
        return round(
            (((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** 0.5, 2
        )
```
### C. Не нажимай красную кнопку!
```python
class RedButton:
    def __init__(self):
        self.value = 0

    def click(self) -> None:
        self.value += 1
        print("Тревога!")

    def count(self) -> int:
        return self.value
```
### D. Работа не волк
```python
class Programmer:
    titles = {"Junior": 10, "Middle": 15, "Senior": 20}
    time = money = 0

    def __init__(self, name: str, position: str) -> None:
        self.name = name
        self.position = position

    def rise(self) -> None:
        if self.position == list(self.titles.keys())[-1]:
            self.titles[list(self.titles.keys())[-1]] += 1
        else:
            self.position = list(self.titles.keys())[
                list(self.titles).index(self.position) + 1
            ]

    def info(self) -> str:
        return f"{self.name} {self.time}ч. {self.money}тгр."

    def work(self, time: int) -> None:
        self.time += time
        self.money += time * self.titles[self.position]
```
### E. Классный прямоугольник
```python
class Rectangle:
    def __init__(
        self, point1: tuple[float, float], point2: tuple[float, float]
    ) -> None:
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
```
### F. Классный прямоугольник 2.0
```python
class Rectangle:
    def __init__(
        self, point1: tuple[float, float], point2: tuple[float, float]
    ) -> None:
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
        self.__init__(
            (self.left_top_x + dx, self.left_top_y + dy),
            (self.right_bottom_x + dx, self.right_bottom_y + dy),
        )

    def resize(self, width: float, height: float) -> None:
        self.__init__(
            self.get_pos(), (self.left_top_x + width, self.left_top_y - height)
        )
```
### G. Классный прямоугольник 3.0
```python
class Rectangle:
    def __init__(
        self, point1: tuple[float, float], point2: tuple[float, float]
    ) -> None:
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
        self.__init__(
            (self.left_top_x + dx, self.left_top_y + dy),
            (self.right_bottom_x + dx, self.right_bottom_y + dy),
        )

    def resize(self, width: float, height: float) -> None:
        self.__init__(
            self.get_pos(), (self.left_top_x + width, self.left_top_y - height)
        )

    def turn(self) -> None:
        delta = (self.width - self.height) / 2
        self.__init__(
            (self.left_top_x + delta, self.left_top_y + delta),
            (self.right_bottom_x - delta, self.right_bottom_y - delta),
        )

    def scale(self, factor: float) -> None:
        self.__init__(
            (
                self.left_top_x - self.width / 2 * (factor - 1),
                self.left_top_y + self.height / 2 * (factor - 1),
            ),
            (
                self.right_bottom_x + self.width / 2 * (factor - 1),
                self.right_bottom_y - self.height / 2 * (factor - 1),
            ),
        )
```
### H. Шашки
```python
class Checkers:
    def __init__(self) -> None:
        self.field: dict[str, Cell] = {}
        positions = [
            column + row for row in "87654321" for column in "ABCDEFGH"
        ]
        statuses = (
            "XBXBXBXBBXBXBXBXXBXBXBXBXXXXXXXXXXXXXXXXWXWXWXWXXWXWXWXWWXWXWXWX"
        )
        for i in range(64):
            self.field[positions[i]] = Cell(statuses[i])

    def move(self, f, t):
        self.field[f], self.field[t] = self.field[t], self.field[f]

    def get_cell(self, position):
        return self.field[position]


class Cell:
    def __init__(self, coordinates: str) -> None:
        self.coordinates = coordinates

    def status(self) -> str:
        return self.coordinates
```
### I. Очередь
```python
class Queue:
    queue = []

    def push(self, item) -> None:
        self.queue.append(item)

    def pop(self) -> None:
        return self.queue.pop(0)

    def is_empty(self) -> int:
        return not len(self.queue)
```
### J. Стек
```python
class Stack:
    stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def is_empty(self) -> int:
        return not len(self.stack)
```
