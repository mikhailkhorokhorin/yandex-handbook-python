def get_repeater(func, count: int):
    def repeater(num: int) -> int:
        for _ in range(count):
            num = func(num)
        return num

    return repeater
