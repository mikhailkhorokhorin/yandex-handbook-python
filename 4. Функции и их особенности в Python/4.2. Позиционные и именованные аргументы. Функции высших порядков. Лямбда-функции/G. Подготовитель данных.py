def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    return sep.join(list(map(str, list(args)))) + end


def get_formatter(sep=" ", end=""):
    return lambda *args: to_string(*args, sep=sep, end=end)
