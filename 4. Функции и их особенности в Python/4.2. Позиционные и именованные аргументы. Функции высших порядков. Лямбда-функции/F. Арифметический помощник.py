def get_operator(op: str):
    res = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "//": lambda a, b: a // b,
        "**": lambda a, b: a**b,
    }
    return res[op]
