lambda item: isinstance(item[1], list) and any(
    x % 2 == 0 for x in item[1] if isinstance(x, int)
)
