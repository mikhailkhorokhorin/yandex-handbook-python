# Ввод и вывод данных. Операции с числами, строками. Форматирование

### Привет, Яндекс!

```python
def main() -> None:
    print("Привет, Яндекс!")


if __name__ == "__main__":
    main()
```

### Привет, всем!

```python
def main() -> None:
    print(f"Привет, {input("Как Вас зовут?\n")}")


if __name__ == "__main__":
    main()
```

### Излишняя автоматизация

```python
def main() -> None:
    string = input()
    print(*[string for _ in range(3)], sep="\n")


if __name__ == "__main__":
    main()
```

### Сдача

```python
def main() -> None:
    print(int(float(input()) - 2.5 * 38))


if __name__ == "__main__":
    main()
```

### Магазин

```python
def main() -> None:
    print(-int(input()) * int(input()) + int(input()))


if __name__ == "__main__":
    main()
```

### Чек

```python
def main() -> None:
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]
    print("Чек")
    print(f"{name} - {weight}кг - {coast}руб/кг")
    print(f"Итого: {weight * coast}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - weight * coast}руб")


if __name__ == "__main__":
    main()
```

### Делу — время, потехе — час

```python
def main() -> None:
    print(*["Купи слона!" for _ in range(int(input()))], sep="\n")


if __name__ == "__main__":
    main()
```

### Наказание

```python
def main() -> None:
    n, message = int(input()), input()
    print(*[f"Я больше никогда не буду писать \"{message}\"!" for _ in range(n)], sep="\n")


if __name__ == "__main__":
    main()
```

### Деловая колбаса

```python
def main() -> None:
    print(int(input()) * int(input()) // 2)


if __name__ == "__main__":
    main()
```

### Детский сад — штаны на лямках

```python
def main() -> None:
    name, number = [input() for _ in range(2)]
    print(f"Группа №{number[0]}.")
    print(f"{number[2]}. {name}.")
    print(f"Шкафчик: {number}.")
    print(f"Кроватка: {number[1]}.")


if __name__ == "__main__":
    main()
```

### Автоматизация игры

```python
def main() -> None:
    num = input()
    print(num[1] + num[0] + num[3] + num[2])


if __name__ == "__main__":
    main()
```

### Интересное сложение

```python
def main() -> None:
    num1, num2 = [int(input()) for _ in range(2)]
    ind2 = (num1 // 100 + num2 // 100) % 10
    ind1 = ((num1 // 10) % 10 + (num2 // 10) % 10) % 10
    ind0 = (num1 % 10 + num2 % 10) % 10
    print(f"{ind2 * 100 + ind1 * 10 + ind0}")


if __name__ == "__main__":
    main()
```

### Дед Мороз и конфеты

```python
def main() -> None:
    candies, in_bag = [int(input()) for _ in range(2)]
    print(in_bag // candies, in_bag % candies, sep="\n")


if __name__ == "__main__":
    main()
```

### Шарики и ручки

```python
def main() -> None:
    red, _, blue = [int(input()) for _ in range(3)]
    print(red + blue + 1)


if __name__ == "__main__":
    main()
```

### В ожидании доставки

```python
def main() -> None:
    n, m, t = [int(input()) for _ in range(3)]
    hours = t // 60
    m += t % 60
    n = (n + hours + m // 60) % 24
    m %= 60
    print(f"{n if n >= 10 else f'0{n}'}:{m if m >= 10 else f'0{m}'}")


if __name__ == "__main__":
    main()
```

### Доставка

```python
def main() -> None:
    print(f"{((-int(input()) + int(input())) / int(input())):.2f}")


if __name__ == "__main__":
    main()

```

### Ошибка кассового аппарата

```python
def main() -> None:
    print(int(input()) + int(input(), 2))


if __name__ == "__main__":
    main()
```

### Сдача 10

```python
def main() -> None:
    print(-int(input(), 2) + int(input()))


if __name__ == "__main__":
    main()
```

### Украшение чека

```python
def main() -> None:
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]
    print("=" * 16 + "Чек" + "=" * 16)
    print("Товар:" + f"{name:>29}")
    print("Цена:" + f"{f"{weight}кг * {coast}руб/кг":>30}")
    print("Итого:" + f"{f"{weight * coast}руб":>29}")
    print("Внесено:" + f"{f"{money}руб":>27}")
    print("Сдача:" + f"{f"{money - weight * coast}руб":>29}")
    print("=" * 35)


if __name__ == "__main__":
    main()
```

### Мухи отдельно, котлеты отдельно

```python
def main() -> None:
    n, m, k1, k2 = [int(input()) for _ in range(4)]
    batch1 = (m * n - n * k2) // (k1 - k2)
    batch2 = n - batch1
    print(batch1, batch2)


if __name__ == "__main__":
    main()
```
