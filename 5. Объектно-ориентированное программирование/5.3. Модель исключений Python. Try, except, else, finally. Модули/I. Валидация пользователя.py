class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def name_validation(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError
    elif sum(
        letter.lower() in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
        for letter in name
    ) != len(name):
        raise CyrillicError
    elif name != name.lower().capitalize():
        raise CapitalError
    return name


def username_validation(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError
    elif sum(
        letter.lower() in "abcdefghijklmnopqrstuvwxyz0123456789_"
        for letter in username
    ) != len(username):
        raise BadCharacterError
    elif username[0] in "0123456789":
        raise StartsWithDigitError
    return username


def user_validation(**kwargs) -> dict:
    keys = list(
        map(
            lambda x: x in ["last_name", "first_name", "username"],
            kwargs.keys(),
        )
    )
    values = list(map(lambda x: isinstance(x, str), kwargs.values()))
    if not all(keys) or len(keys) < 3:
        raise KeyError
    elif not all(values):
        raise TypeError
    name_validation(kwargs["last_name"])
    name_validation(kwargs["first_name"])
    username_validation(kwargs["username"])
    return kwargs
