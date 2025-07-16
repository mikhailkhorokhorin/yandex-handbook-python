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
### F. Кофейня
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
### G. В эфире рубрика «Эксперименты»
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
### H. Длинная сортировка
```python
lambda x: (len(x), x.lower())
```
### I. Чётная фильтрация
```python
lambda x: not sum(map(int, str(x))) % 2
```
### J. Ключевой секрет
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
