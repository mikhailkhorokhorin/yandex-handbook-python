def answer(function):
    def decorated(*args, **kwargs) -> str:
        return f"Результат функции: {function(*args, **kwargs)}"

    return decorated
