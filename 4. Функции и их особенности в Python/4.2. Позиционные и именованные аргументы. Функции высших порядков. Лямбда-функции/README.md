# 4.2. Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции
### A. Генератор списков
```python
def make_list(length: int, value: int = 0) -> list:
    return [value] * length
```
### B. Генератор матриц
```python
def make_matrix(size, value: int = 0) -> list:
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    return [[value for i in range(size[0])] for j in range(size[1])]
```
### C. Функциональный нод 2.0
```python
def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (
            (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
        )
    return num1 + num2


def gcd(*args) -> int:
    args, result = list(args), 0
    for i in range(len(args)):
        result = GCD(result, args[i])
    return result
```
### D. Имя of the month 2.0
```python
def month(num: int, lang: str = "ru") -> str:
    MONTH = {
        "en": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "ru": [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ],
    }
    return MONTH[lang][num - 1]
```
### E. Подготовка данных
```python
def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    return sep.join(list(map(str, list(args)))) + end
```
### F. Арифметический помощник
```python
def get_operator(op: str):
    res = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "//": lambda a, b: a // b,
        "**": lambda a, b: a**b,
    }
    return res[op]
```
### G. Подготовитель данных
```python
def to_string(*args, sep: str = " ", end: str = "\n") -> str:
    return sep.join(list(map(str, list(args)))) + end


def get_formatter(sep=" ", end=""):
    return lambda *args: to_string(*args, sep=sep, end=end)
```
### H. Странный рост
```python
def grow(*args, **kwargs) -> tuple:
    res = list(args)
    for key, value in kwargs.items():
        for i, num in enumerate(list(args)):
            if num % len(key) == 0:
                res[i] += value
    return tuple(res)
```
### I. Странное произведение
```python
def product(*args, **kwargs) -> tuple:
    res = []
    for item in args:
        keys = {key for key in kwargs if key in item}
        if keys:
            prod = 1
            for key in keys:
                prod *= kwargs[key]
            res.append(prod)

    return tuple(res)
```
### J. Наилучший выбор
```python
def choice(*args, **kwargs) -> int:
    if "min" in kwargs:
        f = kwargs["min"]
        g = min
    else:
        f = kwargs["max"]
        g = max
    return g(map(f, args))
```
### K. Кофейня
```python
def order(*args) -> str:
    temp = in_stock
    COFFEE = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for grade in args:
        for ingridient in COFFEE[grade]:
            if COFFEE[grade].get(ingridient, 0) > in_stock[ingridient]:
                break
        else:
            for ingridient in COFFEE[grade]:
                in_stock[ingridient] -= COFFEE[grade][ingridient]
            return grade

    if in_stock == temp:
        return "К сожалению, не можем предложить Вам напиток"
```
### L. В эфире рубрика «Эксперименты»
```python
a = tuple()


def enter_results(*args) -> None:
    global a
    a += args


def get_sum() -> tuple[float, float]:
    return round(sum(a[::2]), 2), round(sum(a[1::2]), 2)


def get_average() -> tuple[float, float]:
    return round(get_sum()[0] / (len(a) // 2), 2), round(
        get_sum()[1] / (len(a) // 2), 2
    )
```
### M. Длинная сортировка
```python
lambda x: (len(x), x.lower())
```
### N. Чётная фильтрация
```python
lambda x: not sum(map(int, str(x))) % 2
```
### O. Повторюшка
```python
def get_repeater(func, count: int):
    def repeater(num: int) -> int:
        for _ in range(count):
            num = func(num)
        return num

    return repeater
```
### P. Обратная связь
```python
def login(username, password, success, error):
    total = sum(ord(i) for i in username) * len(username)
    hex_str = hex(total)[2:]

    if hex_str[::-1].lower() == password.lower():
        success(username)
    else:
        error(username)
```
### Q. Фильтрация словаря
```python
lambda item: isinstance(item[1], list) and any(
    x % 2 == 0 for x in item[1] if isinstance(x, int)
)
```
### R. Преобразование словаря
```python
lambda item: (
    "".join(c for c in item[0].lower() if c.isalpha()),
    (
        sum(item[1])
        if hasattr(item[1], "__iter__")
        and not isinstance(item[1], (str, bytes))
        else item[1]
    ),
)
```
### S. Ключевой секрет
```python
def secret_replace(text: str, **replaces) -> str:
    result, replaces = "", {d: (v, 0) for d, v in replaces.items()}
    print(replaces)
    for i in text:
        if i in replaces:
            result += replaces[i][0][replaces[i][1] % len(replaces[i][0])]
            replaces[i] = replaces[i][0], replaces[i][1] + 1
        else:
            result += i
    return result
```
### T. База данных пользователей
```python
import re
from datetime import datetime

db = []


def insert(*users):
    db.extend(users)


def select(condition=None):
    result = db

    if condition:
        field, op, value = re.split(r"\s*(<=|>=|==|!=|<|>)\s*", condition)

        def convert(val, field_name):
            if field_name == "birth":
                return datetime.strptime(val, "%d.%m.%Y")
            elif field_name == "id":
                return int(val)
            else:
                return val

        value = convert(value, field)
        ops = {
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            ">=": lambda a, b: a >= b,
            "<=": lambda a, b: a <= b,
            "==": lambda a, b: a == b,
            "!=": lambda a, b: a != b,
        }

        result = list(
            filter(
                lambda user: ops[op](convert(user[field], field), value), db
            )
        )

    return sorted(result, key=lambda user: user["id"])
```
