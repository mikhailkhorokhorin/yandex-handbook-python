a = tuple()


def enter_results(*args) -> None:
    global a
    a += args


def get_sum() -> tuple[float, float]:
    return round(sum(a[::2]), 2), round(sum(a[1::2]), 2)


def get_average() -> tuple[float, float]:
    return round(get_sum()[0] / (len(a) // 2), 2), round(
        get_sum()[1] / (len(a) // 2), 2
    )
