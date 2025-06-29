class Queue:
    queue = []

    def push(self, item) -> None:
        self.queue.append(item)

    def pop(self) -> None:
        return self.queue.pop(0)

    def is_empty(self) -> int:
        return not len(self.queue)
