# Рекурсия. Декораторы. Генераторы

### Рекурсивный сумматор

```python
def recursive_sum(*args) -> int:
    return 0 if not args else args[0] + recursive_sum(*args[1:])
```

### Рекурсивный сумматор цифр

```python
def recursive_digit_sum(num: int) -> int:
    return num % 10 + recursive_digit_sum(num // 10) if num != 0 else 0
```

### Многочлен N-ой степени

```python
def make_equation(*args) -> str:
    if len(args) == 1:
        return str(args[0])
    line = ") * x " + ("- " if args[-1] < 0 else "+ ") + str(args[-1])
    return "(" + make_equation(*args[:-1]) 
```

### Декор результата

```python
def answer(function):
    def decorated(*args, **kwargs) -> str:
        return f"Результат функции: {function(*args, **kwargs)}"

    return decorated
```

### Накопление результата

```python
def result_accumulator(func):
    result = []

    def decorated(*args, method: str = "accumulate"):
        result.append(func(*args))
        if method == "drop":
            temp = result.copy()
            result.clear()
            return temp

    return decorated
```

### Сортировка слиянием

```python
def merge(left: list, right: list) -> list:
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array
    return merge(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))
```

### Однотипность не порок

```python
def same_type(function):
    def decorator(*args) -> bool:
        if len(set([type(i) for i in args])) != 1:
            print("Обнаружены различные типы данных")
            return False
        return function(*args)

    return decorator


def fibonacci(num: int) -> int:
    value1, value2 = 0, 1
    for _ in range(num):
        yield value1
        value1, value2 = value2, value1 + value2
```

### Циклический генератор

```python
def cycle(line: list):
    while line:
        for number in line:
            yield number
```

### "Выпрямление" списка

```python
def make_linear(old: list) -> list:
    return [item for i in old for item in (make_linear(i) if isinstance(i, list) else [i])]
```