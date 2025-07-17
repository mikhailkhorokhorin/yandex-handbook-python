def grow(*args, **kwargs) -> tuple:
    res = list(args)
    for key, value in kwargs.items():
        for i, num in enumerate(list(args)):
            if num % len(key) == 0:
                res[i] += value
    return tuple(res)
