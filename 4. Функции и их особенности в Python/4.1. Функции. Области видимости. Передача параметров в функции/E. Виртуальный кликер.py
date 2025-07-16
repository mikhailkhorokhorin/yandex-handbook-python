count = 0


def click() -> None:
    global count
    count += 1


def get_count() -> int:
    return count
