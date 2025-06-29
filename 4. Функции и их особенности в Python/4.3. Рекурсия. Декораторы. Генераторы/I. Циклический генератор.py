def cycle(line: list):
    while line:
        for number in line:
            yield number
