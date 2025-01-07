# Стек
class Stack:
    stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def is_empty(self) -> int:
        return not len(self.stack)
