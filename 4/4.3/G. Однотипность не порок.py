def same_type(function):
    def decorator(*args) -> bool:
        if len(set([type(i) for i in args])) != 1:
            print("Обнаружены различные типы данных")
            return False
        return function(*args)

    return decorator
