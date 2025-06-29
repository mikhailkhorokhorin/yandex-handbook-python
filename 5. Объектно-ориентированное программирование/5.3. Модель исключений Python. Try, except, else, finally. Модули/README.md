# 5.3. Модель исключений Python. Try, except, else, finally. Модули
### A. Обработка ошибок
```python
try:
    func()
except Exception as exception:
    print(type(exception).__name__)
else:
    print("No Exceptions")
```
### B. Ломать — не строить
```python
try:
    func(None, None)
except ValueError:
    print("Ура! Ошибка!")
```
### C. Ломать — не строить 2
```python
class Error:
    def __repr__(self):
        raise ValueError


try:
    func(Error())
except ValueError:
    print("Ура! Ошибка!")
```
### D. Контроль параметров
```python
def only_positive_even_sum(value1, value2) -> int:
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError
    elif not (value1 > 0 and not value1 % 2) or not (
        value2 > 0 and not value2 % 2
    ):
        raise ValueError
    return value1 + value2
```
### E. Слияние с проверкой
```python
def merge(value1, value2):
    if not hasattr(value1, "__iter__") or not hasattr(value2, "__iter__"):
        raise StopIteration
    if not all(
        isinstance(x, type(value1[0])) for x in (list(value1) + list(value2))
    ):
        raise TypeError
    if list(value1) != sorted(value1) or list(value2) != sorted(value2):
        raise ValueError
    return tuple(sorted(list(value1) + list(value2)))
```
### F. Корень зла 2
```python
class InfiniteSolutionsError(Exception):
    pass


class NoSolutionsError(Exception):
    pass


def find_roots(a, b, c) -> tuple[float, float]:
    if sum(1 for i in (a, b, c) if isinstance(i, (int, float)) is True) != 3:
        raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError
    elif (a == b == 0 and c != 0) or b**2 < 4 * a * c:
        raise NoSolutionsError
    elif b**2 == 4 * a * c:
        return -b / (2 * a), -b / (2 * a)
    elif a == 0:
        return -c / b
    else:
        solutions = sorted(
            [
                (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a),
                (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a),
            ]
        )
        return solutions[0], solutions[1]
```
### G. Валидация имени
```python
class CyrillicError(Exception):
    pass


class CapitalError(Exception):
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
```
### H. Валидация имени пользователя
```python
class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


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
```
### I. Валидация пользователя
```python
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
```
### J. Валидация пароля
```python
from hashlib import sha256


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(
    password: str,
    min_length: int = 8,
    possible_chars: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
    at_least_one: bool = str.isdigit,
):
    if not isinstance(password, str):
        raise TypeError
    if len(password) < min_length:
        raise MinLengthError
    if any(i not in possible_chars for i in password):
        raise PossibleCharError
    if not any(map(at_least_one, password)):
        raise NeedCharError
    return sha256(password.encode()).hexdigest()
```
