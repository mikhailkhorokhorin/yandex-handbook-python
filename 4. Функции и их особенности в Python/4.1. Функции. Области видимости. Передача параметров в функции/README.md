# 4.1. Функции. Области видимости. Передача параметров в функции
### A. Функциональное приветствие
```python
def print_hello(name: str) -> None:
    print(f"Hello, {name}!")
```
### B. Функциональный НОД
```python
def gcd(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (
            (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
        )
    return num1 + num2
```
### C. Длина числа
```python
def number_length(num: int) -> int:
    return len(str(abs(num)))
```
### D. Копейка рубль бережёт
```python
def take_small(money: list[int]) -> list[int]:
    return [i for i in money if i < 100]
```
### E. Виртуальный кликер
```python
count = 0


def click() -> None:
    global count
    count += 1


def get_count() -> int:
    return count
```
### F. Странная игра
```python
result = 0


def move(name: str, count: int) -> None:
    global result
    result += count if name == "Петя" else -count


def game_over() -> str:
    return "Петя" if result > 0 else "Ваня" if result < 0 else "Ничья"
```
### G. Максимальный максимум
```python
def max2D(matrix: list[list[int]]) -> int:
    return max([max(i) for i in matrix])
```
### H. Числовое фрагментирование
```python
def fragments(numbers: list[int]):
    result: list[list[int]] = [[numbers[0]]]
    for num in numbers[1:]:
        if num > result[-1][-1]:
            result[-1].append(num)
        else:
            result.append([num])
    return result
```
### I. Имя of the month
```python
def month(num: int, lang: str) -> str:
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
### J. Числовая строка
```python
def split_numbers(line: str) -> tuple:
    return tuple(map(int, line.split()))
```
### K. Поиск гор
```python
def find_mountains(heights: list[int]) -> tuple[int, ...]:
    res = []
    for index, (left, middle, right) in enumerate(
        zip(heights, heights[1:], heights[2:]), 2
    ):
        if middle > left and middle > right:
            res.append(index)
    return tuple(res)
```
### L. Поиск гор 2
```python
from itertools import product


def find_mountains(heights: list[list[int]]) -> tuple[tuple[int, int], ...]:
    n = len(heights)
    m = len(heights[0])
    result = []
    for i, j in product(range(1, n - 1), range(1, m - 1)):
        if all(
            heights[i][j] > heights[k][t]
            for k, t in product(range(i - 1, i + 2), range(j - 1, j + 2))
            if (k, t) != (i, j)
        ):
            result.append((i + 1, j + 1))

    return tuple(result)
```
### M. Модернизация системы вывода
```python
words = []


def modern_print(word: str) -> None:
    print(word) if word not in words else ...
    words.append(word)
```
### N. Шахматный «обед»
```python
def can_eat(knight: tuple[int, int], other: tuple[int, int]) -> bool:
    return abs(knight[0] - other[0]) + abs(knight[1] - other[1]) == 3
```
### O. Словарная строка
```python
def get_dict(text: str) -> dict:
    return {
        k.strip(): (
            int(v.strip())
            if v.strip().lstrip("-").isdigit()
            else (
                float(v.strip())
                if "." in v.strip()
                and v.strip().lstrip("-").replace(".", "", 1).isdigit()
                else v.strip()
            )
        )
        for item in text.split(";")
        if item.strip()
        for k, v in [item.split("=", 1)]
        if "=" in item
    }
```
### P. А роза упала на лапу Азора 7.0
```python
def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]
```
### Q. Простая задача 5.0
```python
def is_prime(num: int) -> bool:
    return (
        sorted(
            {
                i
                for d in range(2, int(num**0.5) + 1)
                if num % d == 0
                for i in (d, num // d)
            }
        )
        == []
    )
```
### R. Слияние
```python
def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    both = list(tuple1) + list(tuple2)
    for i in range(len(both)):
        for j in range(0, len(both) - i - 1):
            if both[j] > both[j + 1]:
                both[j], both[j + 1] = both[j + 1], both[j]
    return tuple(both)
```
### S. Обмен содержимым
```python
def swap(l1: list, l2: list) -> None:
    l1[:], l2[:] = l2[:], l1[:]
```
### T. Цезарю — Цезарево
```python
def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += sym[i]
            n -= val[i]
        i += 1
    return roman_num


def roman(a: int, b: int) -> str:
    a_roman = to_roman(a)
    b_roman = to_roman(b)
    sum_roman = to_roman(a + b)
    return f"{a_roman} + {b_roman} = {sum_roman}"
```
