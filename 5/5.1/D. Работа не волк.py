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
