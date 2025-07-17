def choice(*args, **kwargs) -> int:
    if "min" in kwargs:
        f = kwargs["min"]
        g = min
    else:
        f = kwargs["max"]
        g = max
    return g(map(f, args))
