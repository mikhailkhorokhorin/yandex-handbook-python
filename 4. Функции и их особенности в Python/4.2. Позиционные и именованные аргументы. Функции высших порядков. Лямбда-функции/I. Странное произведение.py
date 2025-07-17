def product(*args, **kwargs) -> tuple:
    res = []
    for item in args:
        keys = {key for key in kwargs if key in item}
        if keys:
            prod = 1
            for key in keys:
                prod *= kwargs[key]
            res.append(prod)

    return tuple(res)
