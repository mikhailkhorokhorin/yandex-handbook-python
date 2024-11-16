def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    a = list(args)
    return sep.join(list(map(str, a))) + end
