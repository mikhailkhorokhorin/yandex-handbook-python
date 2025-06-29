# 3.4. Встроенные возможности по работе с коллекциями
### A. Автоматизация списка
```python
def main() -> None:
    line = input()
    print(
        *[f"{line.split().index(word) + 1}. {word}" for word in line.split()],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### B. Сборы на прогулку
```python
def main() -> None:
    names1, names2 = [input().split(", ") for _ in range(2)]
    print(
        *[
            f"{names1[i]} - {names2[i]}"
            for i in range(min(len(names1), len(names2)))
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### C. Рациональная считалочка
```python
from itertools import count, takewhile


def main() -> None:
    start, end, step = map(float, input().split())
    print(
        *[
            f"{value:.2f}"
            for value in takewhile(lambda x: x <= end, count(start, step))
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### D. Словарная ёлка
```python
from itertools import accumulate


def main() -> None:
    print(
        *[
            word
            for word in accumulate(map(lambda x: x + " ", input().split()))
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### E. Список покупок
```python
def main() -> None:
    for index, product in enumerate(
        sorted({word for _ in range(3) for word in input().split(", ")})
    ):
        print(f"{index + 1}. {product}")


if __name__ == "__main__":
    main()
```
### F. Колода карт
```python
def main() -> None:
    deck, suit = [
        (x, y)
        for x in [*[i for i in range(2, 11)], "валет", "дама", "король", "туз"]
        for y in ["пик", "треф", "бубен", "червей"]
    ], input()
    print(*[f"{x} {y}" for x, y in deck if y != suit], sep="\n")


if __name__ == "__main__":
    main()
```
### G. Игровая сетка
```python
from itertools import combinations


def main() -> None:
    print(
        *[
            f"{x} - {y}"
            for x, y in combinations([input() for _ in range(int(input()))], 2)
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### H. Меню питания 2.0
```python
def main() -> None:
    n = int(input())
    porridge = [input() for _ in range(n)]
    print(*(porridge[i % n] for i in range(int(input()))), sep="\n")


if __name__ == "__main__":
    main()
```
### I. Таблица умножения 3.0
```python
from itertools import product


def main() -> None:
    n = int(input())
    for a1, a2 in product(range(1, n + 1), repeat=2):
        print(a1 * a2, end=" ")
        if a2 == n:
            print()


if __name__ == "__main__":
    main()
```
### J. Мы делили апельсин 2.0
```python
from itertools import product


def main() -> None:
    n = int(input())
    print("А Б В")
    for a, b, c in product(range(1, n + 1), repeat=3):
        print(a, b, c) if a + b + c == n else ...


if __name__ == "__main__":
    main()
```
### K. Числовой прямоугольник 3.0
```python
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for a in range(1, n * m + 1):
        print(f"{a:>{width}}", end=" " if a % m != 0 else "\n")


if __name__ == "__main__":
    main()
```
### L. Список покупок 2.0
```python
def main() -> None:
    products = [x for _ in range(int(input())) for x in input().split(", ")]
    print(
        *[
            f"{index}. {element}"
            for index, element in enumerate(sorted(products), start=1)
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### M. Расстановка спортсменов
```python
from itertools import permutations


def main() -> None:
    print(
        "\n".join(
            ", ".join(a)
            for a in permutations(
                sorted([input() for _ in range(int(input()))])
            )
        )
    )


if __name__ == "__main__":
    main()
```
### N. Спортивные гадания
```python
from itertools import permutations


def main() -> None:
    print(
        "\n".join(
            ", ".join(a)
            for a in permutations(
                sorted([input() for _ in range(int(input()))]), r=3
            )
        )
    )


if __name__ == "__main__":
    main()
```
### O. Список покупок 3.0
```python
from itertools import permutations


def main() -> None:
    for products in permutations(
        sorted([x for _ in range(int(input())) for x in input().split(", ")]),
        3,
    ):
        print(*[" ".join(products)])


if __name__ == "__main__":
    main()
```
### P. Расклад таков...
```python
from itertools import product, permutations


def main() -> None:
    raw_suit = input()
    suits = ["бубен", "пик", "треф", "червей"]
    best_suit = [x for x in suits if x[0] == raw_suit[0]][0]
    nominal = sorted(
        [*[str(x) for x in range(2, 11)], "валет", "дама", "король", "туз"]
    )
    nominal.remove(input())

    card_list = [f"{value} {suit}" for value, suit in product(nominal, suits)]
    card_layout_list = [
        ", ".join(card_layout)
        for card_layout in product(card_list, repeat=3)
        if len(set(card_layout)) == 3
    ]
    print(
        *(
            [
                card_layout
                for card_layout in card_layout_list
                if best_suit in card_layout
            ][:10]
        ),
        sep="\n",
    )


if __name__ == "__main__":
    main()
```
### Q. А есть ещё варианты
```python
from itertools import product, permutations


def main() -> None:
    raw_suit = input()
    suits = ["бубен", "пик", "треф", "червей"]
    best_suit = [x for x in suits if x[0] == raw_suit[0]][0]
    nominal = sorted(
        [*[str(x) for x in range(2, 11)], "валет", "дама", "король", "туз"]
    )
    nominal.remove(input())

    card_layout_tuple = tuple(permutations(product(nominal, suits), r=3))
    card_layout_tuple = (
        ", ".join(" ".join(card_tuple) for card_tuple in sorted(card_layout))
        for card_layout in card_layout_tuple
    )
    card_layout_list = [
        card_layout
        for card_layout in sorted(set(card_layout_tuple))
        if best_suit in card_layout
    ]
    print(card_layout_list[card_layout_list.index(input()) + 1])


if __name__ == "__main__":
    main()
```
### R. Таблица истинности
```python
from itertools import product


def main() -> None:
    print("a b c f")
    f = input()
    for a, b, c in product([0, 1], repeat=3):
        print(a, b, c, int(eval(f)))


if __name__ == "__main__":
    main()
```
### S. Таблица истинности 2
```python
from itertools import product, repeat


def main() -> None:
    f = input()
    print(" ".join(args := sorted({i for i in f if i.isupper()})) + " F")
    for i in product([0, 1], repeat=len(args)):
        print(*i, int(eval(f, dict(zip(args, i)))))


if __name__ == "__main__":
    main()
```
### T. Таблицы истинности 3
```python
from itertools import product


def postfix(
    expression: str, variables: list, operators: dict, priorities: dict
) -> list:
    stack, result = [], []
    for token in expression.split():
        if token in variables:
            result.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                result.append(operators[stack.pop()])
            stack.pop()
        elif token in operators:
            while stack and priorities[token] >= priorities[stack[-1]]:
                result.append(operators[stack.pop()])
            stack.append(token)
    while stack:
        result.append(operators[stack.pop()])
    return result


def result(postfix_exp: list, variables: dict) -> int:
    stack = []
    for token in postfix_exp:
        if token in variables:
            stack.append(variables[token])
        else:
            if token == "not":
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f"{var1} {token} {var2}"))
    return int(stack.pop())


def main() -> None:
    operators = {
        "not": "not",
        "and": "and",
        "or": "or",
        "^": "!=",
        "->": "<=",
        "~": "==",
    }
    priorities = {
        key: value
        for value, key in enumerate(["not", "and", "or", "^", "->", "~", "("])
    }

    statement = input()
    variables = sorted(set(filter(str.isupper, statement)))
    print(" ".join(variables), "F")

    statement = statement.replace("(", "( ").replace(")", " )")
    exp = postfix(statement, variables, operators, priorities)

    for row in product([0, 1], repeat=len(variables)):
        res = dict(zip(variables, row))
        print(" ".join(map(str, row)), result(exp, res))


if __name__ == "__main__":
    main()
```
