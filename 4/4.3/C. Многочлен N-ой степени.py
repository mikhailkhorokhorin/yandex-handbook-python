def make_equation(*args) -> str:
    if len(args) == 1:
        return str(args[0])
    line = ") * x " + ("- " if args[-1] < 0 else "+ ") + str(args[-1])
    return "(" + make_equation(*args[:-1]) + line