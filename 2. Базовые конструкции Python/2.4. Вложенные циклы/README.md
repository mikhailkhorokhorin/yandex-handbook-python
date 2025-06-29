# 2.4. Вложенные циклы
### A. Таблица умножения
```python
def main() -> None:
    for i in range(1, (n := int(input())) + 1):
        print(" ".join(str(i * j) for j in range(1, n + 1)))


if __name__ == "__main__":
    main()
```
### B. Не таблица умножения
```python
def main() -> None:
    for i in range(1, (n := int(input())) + 1):
        print("\n".join(f"{j} * {i} = {i * j}" for j in range(1, n + 1)))


if __name__ == "__main__":
    main()
```
### C. Новогоднее настроение
```python
def main() -> None:
    number = 1
    for i in range(1, (n := int(input())) + 1):
        for j in range(i):
            if number - 1 < n:
                print(number, end=" ")
                number += 1
        print()


if __name__ == "__main__":
    main()
```
### D. Суммарная сумма
```python
def main() -> None:
    print(
        sum(
            [int(i) for x in [input() for _ in range(int(input()))] for i in x]
        )
    )


if __name__ == "__main__":
    main()
```
### E. Зайка — 5
```python
def find() -> int:
    founded = 0
    while (string := input()) != "ВСЁ":
        if string == "зайка":
            founded = 1
    return founded


def main() -> None:
    print(sum([find() for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
```
### F. НОД 2.0
```python
def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (
            (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
        )
    return num1 + num2


def main() -> None:
    numbers = [int(input()) for _ in range(int(input()))]
    gcd = 0
    for i in range(len(numbers)):
        gcd = GCD(gcd, numbers[i])
    print(gcd)


if __name__ == "__main__":
    main()
```
### G. На старт! Внимание! Марш!
```python
def main() -> None:
    for i in range(int(input())):
        print(
            "\n".join(f"До старта {j} секунд(ы)" for j in range(3 + i, 0, -1))
        )
        print(f"Старт {i + 1}!!!")


if __name__ == "__main__":
    main()
```
### H. Максимальная сумма
```python
def main() -> None:
    rating = {}
    for _ in range(int(input())):
        name = input()
        rating[name] = sum([int(x) for x in input()])
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(sorted_rating[0][0])


if __name__ == "__main__":
    main()
```
### I. Большое число
```python
def main() -> None:
    print(
        *[
            max(int(i) for i in x)
            for x in [input() for _ in range(int(input()))]
        ],
        sep="",
    )


if __name__ == "__main__":
    main()
```
### J. Мы делили апельсин
```python
def main() -> None:
    print("А Б В")
    for i in range(1, (n := int(input())) + 1):
        print("\n".join(f"{i} {j} {n - i - j}" for j in range(1, n - i)))


if __name__ == "__main__":
    main()
```
### K. Простая задача 3.0
```python
def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def main() -> None:
    print(sum([is_prime(int(input())) for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
```
### L. Числовой прямоугольник
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(1, n * m + 1):
        print(
            f"{i:>{width}} ",
            end=" " * (i % m == 0) + "\n" * (i % m == 0 and i != n * m),
        )


if __name__ == "__main__":
    main()
```
### M. Числовая змейка
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(
            " ".join(
                f"{i * m + (j + 1 if i % 2 == 0 else m - j):>{width}}"
                for j in range(m)
            )
        )


if __name__ == "__main__":
    main()
```
### N. Числовой прямоугольник 2.0
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(" ".join(f"{i + 1 + j * n:>{width}}" for j in range(m)))


if __name__ == "__main__":
    main()
```
### O. Числовая змейка 2.0
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(
            " ".join(
                f"{j * n + (i + 1 if j % 2 == 0 else n - i):>{width}}"
                for j in range(m)
            )
        )


if __name__ == "__main__":
    main()
```
### P. Редизайн таблицы умножения
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    string = m * n + (n - 1)
    if n != 1:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                k = str(i * j)
                result = f"{k: ^{m}}"
                (
                    print(result, "|", sep="", end="")
                    if j != n
                    else print(result, end="")
                )
            print()
            if i != n:
                print("-" * string)
    else:
        print(f"{1: ^{m}}")


if __name__ == "__main__":
    main()
```
### Q. А роза упала на лапу Азора 3.0
```python
def main() -> None:
    print(
        sum([(string := input()) == string[::-1] for _ in range(int(input()))])
    )


if __name__ == "__main__":
    main()
```
### R. Новогоднее настроение 2.0
```python
def main() -> None:
    n = int(input())
    max_length, number, line = 0, 0, 1
    while number < n:
        length = " ".join(
            str(i) for i in range(number + 1, min(number + line + 1, n + 1))
        )
        max_length = max(len(length), max_length)
        number += line
        line += 1
    number, line = 0, 1
    while number < n:
        answer = " ".join(
            str(i) for i in range(number + 1, min(number + line + 1, n + 1))
        )
        print(f"{answer:^{max_length}}")
        number += line
        line += 1


if __name__ == "__main__":
    main()
```
### S. Числовой квадрат
```python
def main() -> None:
    n = int(input())
    width = len(str(n // 2 + 1))
    for i in range(n):
        print(
            " ".join(
                f"{min(i + 1, n - i, j + 1, n - j):>{width}}" for j in range(n)
            )
        )


if __name__ == "__main__":
    main()
```
### T. Математическая выгода
```python
def main() -> None:
    n = int(input())
    max_i = max_num = 0
    for i in range(2, 11):
        num, s = n, []
        while num > 0:
            s, num = [num % i] + s, num // i
        if max_num < sum(s):
            max_num, max_i = sum(s), i
    print(max_i)


if __name__ == "__main__":
    main()
```
