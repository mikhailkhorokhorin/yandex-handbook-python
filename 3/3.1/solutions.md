# Строки, кортежи, списки

### Азбука

```python
def main() -> None:
    print("YES" if all(input()[0].upper() in "АБВ" for _ in range(int(input()))) else "NO")


if __name__ == "__main__":
    main()
```

### Кручу-верчу

```python
def main() -> None:
    print("\n".join([i for i in input()]))


if __name__ == "__main__":
    main()
```

### Анонс новости

```python
def main():
    n = int(input())
    for _ in range(int(input())):
        print(s[:n - 3:] + "..." if len(s := input()) > n else s)


if __name__ == "__main__":
    main()
```

### Очистка данных

```python
def main() -> None:
    while (s := input()) != "":
        print(s[2::] if s[0:2:] == "###" else s) if s[-1:-4:-1] != "@@@" else ...


if __name__ == "__main__":
    main()
```

### А роза упала на лапу Азора 4.0

```python
def main() -> None:
    print("YES" if (string := input()) == string[::-1] else "NO")


if __name__ == "__main__":
    main()
```

### Зайка — 6

```python
def main() -> None:
    print(sum([input().count("зайка") for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
```

### А и Б сидели на трубе

```python
def main() -> None:
    print(sum(list(map(int, input().split()))))


if __name__ == "__main__":
    main()
```

### Зайка — 7

```python
def main() -> None:
    for _ in range(int(input())):
        print(string.index("зайка") + 1 if "зайка" in (string := input()) else "Заек нет =(")


if __name__ == "__main__":
    main()
```

### Без комментариев

```python
def main() -> None:
    while (string := input()) != "":
        print(string[:string.index("#"):] if "#" in string else string) if string[0] != "#" else ...


if __name__ == "__main__":
    main()
```

### Частотный анализ на минималках

```python
def main() -> None:
    res = ""
    while (s := input()) != 'ФИНИШ':
        res += s
    line = str(res).lower().replace(" ", "")
    count, letter = 0, ""
    for char in set(line):
        if line.count(char) > count:
            letter, count = char, line.count(char)
    print(letter)


if __name__ == "__main__":
    main()
```

### Найдётся всё

```python
def main() -> None:
    headings, request = [input() for _ in range(int(input()))], input()
    print(*[i for i in headings if request.lower() in i.lower()], sep='\n')


if __name__ == "__main__":
    main()
```

### Меню питания

```python
def main() -> None:
    print(*[["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"][i % 5] for i in range(int(input()))], sep="\n")


if __name__ == "__main__":
    main()
```

### Массовое возведение в степень

```python
def main() -> None:
    numbers, power = [int(input()) for _ in range(int(input()))], int(input())
    print(*[i ** power for i in numbers], sep="\n")


if __name__ == "__main__":
    main()
```

### Массовое возведение в степень 2.0

```python
def main() -> None:
    numbers, power = list(map(int, input().split())), int(input())
    print(*[i ** power for i in numbers])


if __name__ == "__main__":
    main()
```

### НОД 3.0

```python
def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def main() -> None:
    numbers = list(map(int, input().split()))
    gcd = 0
    for i in range(len(numbers)):
        gcd = GCD(gcd, numbers[i])
    print(gcd)


if __name__ == "__main__":
    main()
```

### Анонс новости 2.0

```python
def main() -> None:
    length, strings = int(input()), [input() for _ in range(int(input()))]
    total = length
    for i in strings:
        if total <= 3:
            break
        print(i[:total:] if (total - len(i)) > 3 else i[:total - 3:] + "...")
        total -= len(i)


if __name__ == "__main__":
    main()
```

### А роза упала на лапу Азора 5.0

```python
def main() -> None:
    print("YES" if (string := input().replace(" ", "").lower()) == string[::-1] else "NO")


if __name__ == "__main__":
    main()
```

### RLE

```python
def main() -> None:
    line = input()
    letter, count = line[0], 1
    for i in line[1:]:
        if i == letter:
            count += 1
        else:
            print(letter, count)
            letter, count = i, 1
    print(letter, count)


if __name__ == "__main__":
    main()
```

### Польский калькулятор

```python
def main() -> None:
    elements, result = list(input().split()), []
    for i in elements:
        if i.isdigit():
            result.append(int(i))
        else:
            a = result.pop()
            exec("result[-1] " + i + "= a")
    print(*result)


if __name__ == "__main__":
    main()
```

### Польский калькулятор — 2

```python
def f(n: int) -> int:
    return n * f(n - 1) if n > 1 else 1


def main() -> None:
    elements = list(input().split())
    result = []
    for i in elements:
        if i.isdigit():
            result.append(int(i))
        elif i == '~':
            result[-1] *= -1
        elif i == "!":
            result[-1] = f(result[-1])
        elif i == "#":
            result.append(result[-1])
        elif i == "/":
            a = result.pop()
            result[-1] //= a
        elif i == "@":
            a = result.pop(-3)
            result.append(a)
        else:
            a = result.pop()
            exec("result[-1] " + i + "=a")
    print(*result)


if __name__ == "__main__":
    main()
```