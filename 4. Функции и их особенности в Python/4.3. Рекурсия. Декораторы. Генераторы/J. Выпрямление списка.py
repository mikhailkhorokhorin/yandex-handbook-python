def make_linear(old: list) -> list:
    return [
        item for i in old for item in (make_linear(i) if isinstance(i, list) else [i])
    ]
