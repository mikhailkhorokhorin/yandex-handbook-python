# 2.2. Условный оператор
### A. Просто здравствуй, просто как дела
```python
def main() -> None:
    print(f"Здравствуйте, {input("Как Вас зовут?\n")}!")
    print(
        "Я за вас рада!"
        if input("Как дела?\n") == "хорошо"
        else "Всё наладится!"
    )


if __name__ == "__main__":
    main()
```
### B. Кто быстрее
```python
def main() -> None:
    print("Петя" if int(input()) > int(input()) else "Вася")


if __name__ == "__main__":
    main()
```
### C. Кто быстрее на этот раз
```python
def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(sorted_rating[0][0])


if __name__ == "__main__":
    main()
```
### D. Список победителей
```python
def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(*[f"{i + 1}. {sorted_rating[i][0]}" for i in range(3)], sep="\n")


if __name__ == "__main__":
    main()
```
### E. Яблоки
```python
def main() -> None:
    print(
        "Петя"
        if 7 - 3 + 2 + int(input()) > 6 + 3 + 5 - 2 + int(input())
        else "Вася"
    )


if __name__ == "__main__":
    main()
```
### F. Сила прокрастинации
```python
def main() -> None:
    year = int(input())
    print(
        "YES"
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        else "NO"
    )


if __name__ == "__main__":
    main()
```
### G. А роза упала на лапу Азора
```python
def main() -> None:
    print("YES" if (number := input()) == number[::-1] else "NO")


if __name__ == "__main__":
    main()
```
### H. Зайка — 1
```python
def main() -> None:
    print("YES" if "зайка" in input() else "NO")


if __name__ == "__main__":
    main()
```
### I. Первому игроку приготовиться
```python
def main() -> None:
    print(min(input(), input(), input()))


if __name__ == "__main__":
    main()
```
### J. Лучшая защита — шифрование
```python
def main() -> None:
    number = int(input())
    ind1 = number % 10 + (number // 10) % 10
    ind0 = number // 100 + (number // 10) % 10
    print(f"{ind1}{ind0}" if ind1 >= ind0 else f"{ind0}{ind1}")


if __name__ == "__main__":
    main()
```
### K. Красота спасёт мир
```python
def main() -> None:
    n = sorted([int(x) for x in input()])
    print("YES" if n[2] + n[0] == n[1] * 2 else "NO")


if __name__ == "__main__":
    main()
```
### L. Музыкальный инструмент
```python
def main() -> None:
    side1, side2, side3 = [int(input()) for _ in range(3)]
    print(
        "YES"
        if (side1 < side2 + side3)
        and (side2 < side1 + side3)
        and (side3 < side1 + side2)
        else "NO"
    )


if __name__ == "__main__":
    main()
```
### M. Властелин Чисел. Братство общей цифры
```python
def main() -> None:
    num1, num2, num3 = [int(input()) for _ in range(3)]
    print(
        num1 // 10
        if (num1 // 10) == (num2 // 10) == (num3 // 10)
        else num1 % 10
    )


if __name__ == "__main__":
    main()
```
### N.  Властелин Чисел. Две Башни
```python
def main() -> None:
    number = input()
    raw_combinations = [
        number[i] + number[j]
        for i in range(len(number))
        for j in range(len(number))
        if i != j
    ]
    combinations = sorted([int(i) for i in raw_combinations if i[0] != "0"])
    print(combinations[0], combinations[-1])


if __name__ == "__main__":
    main()
```
### O. Властелин Чисел. Возвращение Цезаря
```python
def main() -> None:
    num1, num2 = input(), input()
    combinations = sorted(
        [int(x) for x in (num1[0], num1[1], num2[0], num2[1])]
    )
    print(
        f"{combinations[-1]}{(sum(combinations) - combinations[-1] - combinations[0]) % 10}{combinations[0]}"
    )


if __name__ == "__main__":
    main()
```
### P. Легенды велогонок возвращаются. кто быстрее
```python
def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]

    print(f"{f"{sorted_rating[0][0]}":^24}")
    print(f"{f"{sorted_rating[1][0]}":^8}")
    print(" " * 16 + f"{f"{sorted_rating[2][0]}":^8}")
    print(f"{"II":^8}" + f"{"I":^8}" + f"{"III":^8}")


if __name__ == "__main__":
    main()
```
### Q. Корень зла
```python
def main() -> None:
    a, b, c = [float(input()) for _ in range(3)]

    if a == b == c == 0:
        print("Infinite solutions")
    elif (a == b == 0 and c != 0) or b**2 < 4 * a * c:
        print("No solution")
    elif b**2 == 4 * a * c:
        print(f"{-b / (2 * a):.2f}")
    elif a == 0:
        print(f"{-c / b:.2f}")
    else:
        solutions = sorted(
            [
                (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a),
                (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a),
            ]
        )
        print(f"{solutions[0]:.2f} {solutions[1]:.2f}")


if __name__ == "__main__":
    main()
```
### R. Территория зла
```python
def main() -> None:
    side1, side2, c = [int(input()) for _ in range(3)]
    if (
        (side1**2 == side2**2 + c**2)
        or (side2**2 == side1**2 + c**2)
        or (c**2 == side1**2 + side2**2)
    ):
        print("100%")
    elif (
        (side1**2 > side2**2 + c**2)
        or (side2**2 > side1**2 + c**2)
        or (c**2 > side1**2 + side2**2)
    ):
        print("велика")
    else:
        print("крайне мала")


if __name__ == "__main__":
    main()
```
### S. Автоматизация безопасности
```python
def main() -> None:
    x, y = [float(input()) for _ in range(2)]

    rectangle = y <= 5
    circle = x**2 + y**2 <= 25
    parable = y >= 0.25 * (x + 1) ** 2 - 9
    triangle = y <= (5 / 3) * x + (35 / 3)

    if rectangle and circle and parable and triangle:
        print("Опасность! Покиньте зону как можно скорее!")
    elif x**2 + y**2 >= 100:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")


if __name__ == "__main__":
    main()
```
### T. Зайка — 2
```python
def main() -> None:
    result = min([i for i in ([input() for _ in range(3)]) if "зайка" in i])
    print(result, len(result))


if __name__ == "__main__":
    main()
```
