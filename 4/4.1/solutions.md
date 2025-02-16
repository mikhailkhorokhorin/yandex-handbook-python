# Функции. Области видимости. Передача параметров в функции

### Функциональное приветствие

```python
def print_hello(name: str) -> None:
    print(f"Hello, {name}!")
```

### Функциональный НОД

```python
def gcd(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2
```

### Длина числа

```python
def number_length(num: int) -> int:
    return len(str(abs(num)))
```

### Имя of the month

```python
def month(num: int, lang: str) -> str:
    MONTH = {
        "en": [
            "January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"],
        "ru": [
            "Январь", "Февраль", "Март",
            "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь",
            "Октябрь", "Ноябрь", "Декабрь"]}
    return MONTH[lang][num - 1]
```

### Числовая строка

```python
def split_numbers(line: str) -> tuple:
    return tuple(map(int, line.split()))
```

### Модернизация системы вывода

```python
words = []


def modern_print(word: str) -> None:
    print(word) if word not in words else ...
    words.append(word)
```

### Шахматный «обед»

```python
def can_eat(knight: tuple[int, int], other: tuple[int, int]) -> bool:
    return abs(knight[0] - other[0]) + abs(knight[1] - other[1]) == 3
```

### А роза упала на лапу Азора 7.0

```python
def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1] if isinstance(n, int) else n == n[::-1]
```

### Простая задача 5.0

```python
def is_prime(num: int) -> bool:
    return sorted({i for d in range(2, int(num ** 0.5) + 1) if num % d == 0 for i in (d, num // d)}) == []
```

### Слияние

```python
def merge(tuple1: tuple, tuple2: tuple) -> tuple:
    both = list(tuple1) + list(tuple2)
    for i in range(len(both)):
        for j in range(0, len(both) - i - 1):
            if both[j] > both[j + 1]:
                both[j], both[j + 1] = both[j + 1], both[j]
    return tuple(both)
```