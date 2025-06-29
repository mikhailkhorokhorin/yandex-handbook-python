# 3.2. Множества, словари
### A. Символическая выжимка
```python
def main() -> None:
    print(*set(input()), sep="")


if __name__ == "__main__":
    main()
```
### B. Символическая разница
```python
def main() -> None:
    print(*(set(input()) & set(input())), sep="")


if __name__ == "__main__":
    main()
```
### C. Зайка — 8
```python
def main() -> None:
    elements = []
    for _ in range(int(input())):
        elements.extend(input().split())
    print(*set(elements), sep="\n")


if __name__ == "__main__":
    main()
```
### D. Кашееды
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    semolina = set([input() for _ in range(n)])
    oatmeal = set([input() for _ in range(m)])
    print(len(both) if len(both := (semolina & oatmeal)) else "Таких нет")


if __name__ == "__main__":
    main()
```
### E. Кашееды — 2
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    names = [input() for _ in range(n + m)]
    names = [i for i in names if names.count(i) == 1]
    print(len(names) if len(names) else "Таких нет")


if __name__ == "__main__":
    main()
```
### F. Кашееды — 3
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    names = [input() for _ in range(n + m)]
    names = [i for i in names if names.count(i) == 1]
    print(*(sorted(names)), sep="\n") if len(names) else print("Таких нет")


if __name__ == "__main__":
    main()
```
### G. Азбука Морзе
```python
def main() -> None:
    Morse = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    print(
        *[Morse[i] + " " if i in Morse else "\n" for i in input().upper()],
        sep="",
        end="",
    )


if __name__ == "__main__":
    main()
```
### H. Кашееды — 4
```python
def main() -> None:
    list = {}
    for i in range(int(input())):
        string = input().split()
        name, porridge = string[0], string[1:]
        for j in porridge:
            list.setdefault(j, []).append(name)
    (
        print(*(sorted(list[n])), sep="\n")
        if (n := input()) in list
        else print("Таких нет")
    )


if __name__ == "__main__":
    main()
```
### I. Зайка — 9
```python
def main() -> None:
    words = []
    while (string := input()) != "":
        words.extend(string.split())
    print(*[f"{word} {words.count(word)}" for word in set(words)], sep="\n")


if __name__ == "__main__":
    main()
```
### J. Транслитерация
```python
def main() -> None:
    alphabet = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
        "Ь": "",
        "Ъ": "",
    }
    for letter in input():
        if letter.upper() in "ЬЪ":
            continue
        elif letter.upper() in alphabet:
            if letter.isupper():
                print(
                    alphabet[letter][0].upper() + alphabet[letter][1:].lower(),
                    end="",
                )
            else:
                print(alphabet[letter.upper()].lower(), end="")
        else:
            print(letter, end="")


if __name__ == "__main__":
    main()
```
### K. Однофамильцы
```python
def main() -> None:
    surnames = [input() for _ in range(int(input()))]
    print(
        sum(
            [
                surnames.count(i)
                for i in set(surnames)
                if surnames.count(i) != 1
            ]
        )
    )


if __name__ == "__main__":
    main()
```
### L. Однофамильцы — 2
```python
def main() -> None:
    surnames = [input() for _ in range(int(input()))]
    namesakes = sorted(set([x for x in surnames if surnames.count(x) != 1]))
    (
        print(*[f"{i} - {surnames.count(i)}" for i in namesakes], sep="\n")
        if namesakes
        else print("Однофамильцев нет")
    )


if __name__ == "__main__":
    main()
```
### M. Дайте чего-нибудь новенького!
```python
def main() -> None:
    menu = [input() for _ in range(int(input()))]
    cooked = []
    for _ in range(int(input())):
        cooked.extend([input() for _ in range(int(input()))])
    (
        print(*other, sep="\n")
        if (other := sorted(set(menu) - set(cooked)))
        else print("Готовить нечего")
    )


if __name__ == "__main__":
    main()
```
### N. Это будет шедевр!
```python
def main() -> None:
    products = [input() for _ in range(int(input()))]
    dishes, can_cook = {}, []
    for _ in range(int(input())):
        name = input()
        dishes[name] = [input() for _ in range(int(input()))]
        (
            can_cook.append(name)
            if len(set(dishes[name]) - set(products)) == 0
            else ...
        )
    (
        print(*sorted(can_cook), sep="\n")
        if can_cook
        else print("Готовить нечего")
    )


if __name__ == "__main__":
    main()
```
### O. Двоичная статистика!
```python
def main() -> None:
    result = []
    for i in [bin(x)[2:] for x in map(int, input().split())]:
        result.append(
            {"digits": len(i), "units": i.count("1"), "zeros": i.count("0")}
        )
    print(result)


if __name__ == "__main__":
    main()
```
### P. Зайка — 10
```python
def main() -> None:
    result = []
    while string := input().split():
        if "зайка" in string:
            index = 0
            for i in range(string.count("зайка")):
                index = string.index("зайка", index + i)
                if index == 0 and len(string) > 1:
                    result.append(string[index + 1])
                elif index == (len(string) - 1):
                    result.append(string[index - 1])
                else:
                    result.append(string[index - 1])
                    result.append(string[index + 1])
    print(*set(result), sep="\n")


if __name__ == "__main__":
    main()
```
### Q. Друзья друзей
```python
def main() -> None:
    close_friends = {}
    while (string := input()) != "":
        surname1, surname2 = string.split()
        close_friends.setdefault(surname1, []).append(surname2)
        close_friends.setdefault(surname2, []).append(surname1)

    friends, pairs = {x: [] for x in set(close_friends.keys())}, []

    for key, value in close_friends.items():
        for friend_key in value:
            if (key, friend_key) not in pairs:
                pairs.extend([(key, friend_key), (friend_key, key)])
                friends[key].extend(close_friends[friend_key])
                friends[friend_key].extend(close_friends[key])

    for i in friends:
        friends[i] = [
            x for x in set(friends[i]) if x != i and x not in close_friends[i]
        ]

    for i in sorted(friends):
        print(f"{i}: {', '.join(sorted(friends[i]))}")


if __name__ == "__main__":
    main()
```
### R. Карта сокровищ
```python
def main() -> None:
    result = {}
    for _ in range(int(input())):
        cords = input().split()
        x = f"{cords[0][:-1]}-{cords[1][:-1]}"
        result[x] = result.get(x, 0) + 1
    print(max(result.values()))


if __name__ == "__main__":
    main()
```
### S. Частная собственность
```python
def main() -> None:
    result = []
    for i in range(int(input())):
        result.extend(set(input().split(": ")[1].split(", ")))
    result = [x for x in result if result.count(x) == 1]
    print(*(sorted(result)), sep="\n")


if __name__ == "__main__":
    main()
```
### T. Простая задача 4.0
```python
def LCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (
            (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
        )
    return num1 + num2


def main() -> None:
    string = sorted(set(map(int, input().split("; "))))
    result = {str(i): [] for i in string}
    for i in string:
        result[str(i)].extend(
            str(j) for j in string if i != j and LCD(i, j) == 1
        )
        if result[str(i)]:
            print(f"{i} - {', '.join(result[str(i)])}")


if __name__ == "__main__":
    main()
```
