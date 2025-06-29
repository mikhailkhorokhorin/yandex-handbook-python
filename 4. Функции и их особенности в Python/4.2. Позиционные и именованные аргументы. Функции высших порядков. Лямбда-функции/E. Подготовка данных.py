def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    return sep.join(list(map(str, list(args)))) + end
