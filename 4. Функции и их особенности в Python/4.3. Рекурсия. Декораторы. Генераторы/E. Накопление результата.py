def result_accumulator(func):
    result = []

    def decorated(*args, method: str = "accumulate"):
        result.append(func(*args))
        if method == "drop":
            temp = result.copy()
            result.clear()
            return temp

    return decorated
