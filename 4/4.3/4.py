def answer(function):
    def decorated(*args, **kwargs):
        return f"Результат функции: {function(*args, **kwargs)}"

    return decorated
