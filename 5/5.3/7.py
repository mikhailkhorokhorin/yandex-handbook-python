# Валидация имени
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif sum(letter.lower() in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for letter in name) != len(name):
        raise CyrillicError
    elif name != name.lower().capitalize():
        raise CapitalError
    return name
