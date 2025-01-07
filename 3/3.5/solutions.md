# Потоковый ввод/вывод. Работа с текстовыми файлами. JSON

### A+B+...

```python
from sys import stdin


def main() -> None:
    print(sum(map(int, stdin.read().split())))


if __name__ == "__main__":
    main()
```

### Средний рост

```python
from sys import stdin


def main() -> None:
    print(round(sum(x := [int(line.split()[2]) - int(line.split()[1]) for line in stdin.readlines()]) / len(x)))


if __name__ == "__main__":
    main()
```

### Без комментариев 2.0

```python
from sys import stdin


def main() -> None:
    print(*[i[0:i.find("#")] for i in stdin.readlines() if not i[0] == "#"], sep="\n")


if __name__ == "__main__":
    main()
```

### Найдётся всё 2.0

```python
from sys import stdin


def main() -> None:
    x = [i.strip() for i in stdin]
    print(*[line for line in x[:-1] if x[-1].lower() in line.lower()], sep="\n")


if __name__ == "__main__":
    main()
```

### А роза упала на лапу Азора 6.0

```python
from sys import stdin


def main() -> None:
    data = [string.strip().split() for string in stdin]
    words = [word for line in data for word in line if word.lower() == word.lower()[::-1]]
    print(*sorted(set(words)), sep="\n")


if __name__ == "__main__":
    main()
```

### Транслитерация 2.0

```python
def main() -> None:
    alphabet = {
        "А": "A", "Б": "B", "В": "V",
        "Г": "G", "Д": "D", "Е": "E",
        "Ё": "E", "Ж": "ZH", "З": "Z",
        "И": "I", "Й": "I", "К": "K",
        "Л": "L", "М": "M", "Н": "N",
        "О": "O", "П": "P", "Р": "R",
        "С": "S", "Т": "T", "У": "U",
        "Ф": "F", "Х": "KH", "Ц": "TC",
        "Ч": "CH", "Ш": "SH", "Щ": "SHCH",
        "Ы": "Y", "Э": "E", "Ю": "IU",
        "Я": "IA", "Ь": "", "Ъ": "",
        }
    data, translit_data = "", ""
    with open("cyrillic.txt", encoding="UTF-8") as file:
        for line in file:
            data += line

    for i in data:
        if i.upper() in alphabet:
            translit_data += alphabet[i.upper()].lower().capitalize() if i == i.upper() else alphabet[i.upper()].lower()
        else:
            translit_data += i

    with open("transliteration.txt", "w", encoding="UTF-8") as file:
        print(translit_data, file=file)


if __name__ == "__main__":
    main()
```

### Файловая статистика

```python
def main() -> None:
    numbers = []
    with open(input(), "r") as file:
        for line in file:
            numbers.extend([int(x) for x in line.split()])
    statistics = [len(numbers), len([x for x in numbers if x > 0]), min(numbers), max(numbers), sum(numbers),
                  round(sum(numbers) / len(numbers), 2)]
    print(*statistics, sep="\n")


if __name__ == "__main__":
    main()
```

### Файловая разница

```python
def main() -> None:
    input_files = [input() for _ in range(2)]
    output_file = input()
    data = [set(), set()]
    for i in range(2):
        with open(input_files[i], "r") as file:
            for line in file:
                data[i].update({x for x in line.split()})

    with open(output_file, "w") as file:
        for word in sorted(data[0] ^ data[1]):
            print(word, file=file)


if __name__ == "__main__":
    main()
```

### Файловая чистка

```python
def main() -> None:
    input_file, output_file = [input() for _ in range(2)]
    data = []
    with open(input_file, "r") as file:
        for line in file:
            data.append(line.strip().replace("\t", "").split())
    data = [x for x in data if any(x)]
    with open(output_file, "w") as file:
        for line in data:
            print(" ".join(line), file=file)


if __name__ == "__main__":
    main()
```

### Хвост

```python
def main() -> None:
    f, n = input(), int(input())
    data = []
    with open(f, "r") as f:
        for line in f:
            data.append(line)
    for line in data[-n:]:
        print(line.strip())


if __name__ == "__main__":
    main()
```

### Файловая статистика 2.0

```python
import json


def main() -> None:
    file_in, file_out = [input() for _ in range(2)]
    numbers = []
    with open(file_in, "r") as file:
        for line in file:
            numbers.extend([int(x) for x in line.split()])
    data = {
        "count": len(numbers),
        "positive_count": len([x for x in numbers if x > 0]),
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2)}
    with open(file_out, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
```

### Разделяй и властвуй

```python
def compare(numbers: list) -> int:
    odd = sum(1 for x in numbers if int(x) % 2 == 0)
    even = len(numbers) - odd
    return 0 if odd > even else 1 if odd < even else 2


def main() -> None:
    numbers, even, odd, eq = [input() for _ in range(4)]
    lines, k = [], 0
    with open(numbers, encoding="UTF-8") as file:
        for line in file:
            lines.append([x for x in line.split()])
    for t in even, odd, eq:
        with open(t, "w", encoding="UTF-8") as file:
            for i in range(len(lines)):
                for j in lines[i]:
                    if compare(j) == k:
                        print(j, end=" ", file=file)
                print("", file=file)
        k += 1


if __name__ == "__main__":
    main()
```

### Обновление данных

```python
import json
from sys import stdin


def main() -> None:
    with open(user := input(), encoding="UTF-8") as file:
        data = json.load(file)
    for line in stdin:
        before = line[:line.find("=")].rstrip()
        after = line[line.find("==") + 2:].lstrip()
        data[before] = after.rstrip()
    with open(user, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
```

### Слияние данных

```python
import json


def main() -> None:
    files = [input() for _ in range(2)]
    data = [{}, {}]
    for i in range(2):
        with open(files[i], "r") as file:
            data[i] = json.load(file)

    data[0] = {i["name"]: {key: value for key, value in i.items() if key != "name"} for i in data[0]}
    for param in data[1]:
        if param["name"] in data[0]:
            for key in param:
                if (key not in data[0][param["name"]] or param[key] > data[0][param["name"]][key]) and key != "name":
                    data[0][param["name"]][key] = param[key]
        else:
            data[0][param["name"]] = {key: value for key, value in param.items() if key != "name"}

    with open(files[0], "w") as file:
        json.dump(data[0], file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
```

### Поставь себя на моё место

```python
from sys import stdin
import json


def main() -> None:
    user = [x.strip() for x in stdin]
    with open("scoring.json", encoding="UTF-8") as f:
        data = json.load(f)
    points = count = 0
    data = [{test["pattern"]: block["points"] // len(block["tests"]) for test in block["tests"]} for block in data]
    for i in data:
        for j in range(count, len(i) + count):
            if user[j] in i:
                points += i[user[j]]
            count += 1
    print(points)


if __name__ == "__main__":
    main()
```

### Найдётся всё 3.0

```python
from sys import stdin


def clear(string: str) -> str:
    string = string.replace("\n", " ")
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def main() -> None:
    string, flag = input(), True
    files = [x.strip() for x in stdin]
    for name in files:
        with open(name, encoding="UTF-8") as file:
            data = "".join(file.readlines()).lower()
            if string.lower() in clear(data):
                print(name)
                flag = False
    print("404. Not Found") if flag else ...


if __name__ == "__main__":
    main()
```

### Прятки

```python
def main() -> None:
    with open("secret.txt", "r", encoding="UTF-8") as file:
        for symbol in file.read():
            print(chr(ord(symbol) % 128), end="")


if __name__ == "__main__":
    main()
```

### Сколько вешать в байтах?

```python
import os
import math


def main() -> None:
    size, postfixes, index = os.path.getsize(input()), ["Б", "КБ", "МБ", "ГБ"], 0
    while size >= 1024 and index < len(postfixes) - 1:
        size = math.ceil(size / 1024)
        index += 1
    print(size, postfixes[index], sep="")


if __name__ == "__main__":
    main()
```

### Это будет наш секрет

```python
def main() -> None:
    shift = int(input())
    alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
    with open("public.txt", encoding="UTF-8") as file:
        data = file.read()
    words = [x.lower() for x in data]
    res = [alphabet[(alphabet.find(x.lower()) + shift) % 26] if x in alphabet else x for x in words]
    for x in range(len(res)):
        if data[x].isupper():
            res[x] = res[x].upper()
    with open("private.txt", "w", encoding="UTF-8") as file:
        print(''.join(x for x in res), file=file)


if __name__ == "__main__":
    main()
```

### Файловая сумма

```python
def main() -> None:
    with open("numbers.num", "rb") as file:
        numbers = file.read()
    print(sum([int.from_bytes(numbers[i:i + 2], "big") for i in range(0, len(numbers), 2)]) % 2 ** 16)


if __name__ == "__main__":
    main()
```