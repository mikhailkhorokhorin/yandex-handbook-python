class RedButton:
    def __init__(self):
        self.value = 0

    def click(self) -> None:
        self.value += 1
        print("Тревога!")

    def count(self) -> int:
        return self.value