# Валидация имени пользователя
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError
    elif sum(letter.lower() in "abcdefghijklmnopqrstuvwxyz0123456789_" for letter in username) != len(username):
        raise BadCharacterError
    elif username[0] in "0123456789":
        raise StartsWithDigitError
    return username
