# Циклы

### A. Раз, два, три! Ёлочка, гори!

```python
def main() -> None:
    while input() != "Три!":
        print("Режим ожидания...")
    print("Ёлочка, гори!")


if __name__ == "__main__":
    main()
```

### B. Зайка — 3

```python
def main() -> None:
    count = 0
    while (string := input()) != "Приехали!":
        count += 1 if "зайка" in string else ...
    print(count)


if __name__ == "__main__":
    main()
```

### C. Считалочка

```python
def main() -> None:
    print(*[i for i in range(int(input()), int(input()) + 1)], end=" ")


if __name__ == "__main__":
    main()
```

### D. Считалочка 2.0

```python
def main() -> None:
    start, end = [int(input()) for _ in range(2)]
    step = 1 if start < end else -1
    print(*[i for i in range(start, end + step, step)], end=" ")


if __name__ == "__main__":
    main()
```

### E. Внимание! Акция!

```python
def main() -> None:
    discount = full_coast = 0
    while (s := float(input())) != 0:
        discount += s * (s >= 500)
        full_coast += s * (s < 500)
    print(full_coast + discount * 9 / 10)


if __name__ == "__main__":
    main()
```

### F. НОД

```python
def main() -> None:
    num1, num2 = [int(input()) for _ in range(2)]
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    print(num1 + num2)


if __name__ == "__main__":
    main()
```

### G. НОК

```python
def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def main() -> None:
    num1, num2 = [int(input()) for _ in range(2)]
    print(num1 * num2 // GCD(num1, num2))


if __name__ == "__main__":
    main()
```

### H. Излишняя автоматизация 2.0

```python
def main() -> None:
    string = input()
    for _ in range(int(input())):
        print(string)


if __name__ == "__main__":
    main()
```

### I. Факториал

```python
def f(n: int) -> int:
    return n * f(n - 1) if n > 1 else 1


def main() -> None:
    print(f(int(input())))


if __name__ == "__main__":
    main()
```

### J. Маршрут построен

```python
def main() -> None:
    x = y = 0
    x_dir = {"ВОСТОК": 1, "ЗАПАД": -1}
    y_dir = {"СЕВЕР": 1, "ЮГ": -1}

    while (direction := input()) != "СТОП":
        value = int(input())
        (x, y) = (x + value * x_dir[direction], y) if direction in x_dir else (x, y + value * y_dir[direction])
    print(y, x, sep="\n")


if __name__ == "__main__":
    main()
```

### K. Цифровая сумма

```python
def main() -> None:
    print(sum([int(i) for i in input()]))


if __name__ == "__main__":
    main()
```

### L. Сильная цифра

```python
def main() -> None:
    print(max([int(i) for i in input()]))


if __name__ == "__main__":
    main()
```

### M. Первому игроку приготовиться 2.0

```python
def main() -> None:
    print(min([input() for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
```

### N. Простая задача

```python
def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def main() -> None:
    print("YES" if is_prime(int(input())) else "NO")


if __name__ == "__main__":
    main()
```

### O. Зайка - 4

```python
def main() -> None:
    print(sum([1 for _ in range(int(input())) if "зайка" in input()]))


if __name__ == "__main__":
    main()
```

### P. А роза упала на лапу Азора 2.0

```python
def main() -> None:
    print("YES" if (number := input()) == number[::-1] else "NO")


if __name__ == "__main__":
    main()
```

### Q. Чётная чистота

```python
def main() -> None:
    print(*[int(i) for i in input() if int(i) % 2 != 0], sep="")


if __name__ == "__main__":
    main()
```

### R. Простая задача 2.0

```python
def main() -> None:
    number, multipliers, divider = int(input()), [], 2
    print(number) if number < 2 else ...

    while number > 1:
        if number % divider == 0:
            multipliers.append(divider)
            number //= divider
        else:
            divider += 1

    print(*multipliers, sep=" * ")


if __name__ == "__main__":
    main()
```

### S. Игра в «Угадайку»

```python
def main() -> None:
    number, half = 500, 250
    print(number)
    while (string := input()) != "Угадал!":
        number += half if string == "Больше" else -half if string == "Меньше" else 0
        half = (half + 1) // 2 if half >= 2 else ...
        print(number)


if __name__ == "__main__":
    main()
```

### T. Хайпанём немножечко!

```python
def main() -> None:
    result, hn = -1, 0
    for i in range(int(input())):
        b = int(input())
        h = b % 256
        r = (b // 256) % 256
        m = b // (256 ** 2)
        temp = 37 * (hn + r + m) % 256
        if temp != h or h >= 100:
            result = i
            break
        hn = h
    print(result)


if __name__ == "__main__":
    main()
```