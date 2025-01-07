# Шашки
class Checkers:
    def __init__(self) -> None:
        self.field: dict[str, Cell] = {}
        positions = [column + row for row in "87654321" for column in "ABCDEFGH"]
        statuses = "XBXBXBXBBXBXBXBXXBXBXBXBXXXXXXXXXXXXXXXXWXWXWXWXXWXWXWXWWXWXWXWX"
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
