# Таблица истинности 2
from itertools import product, repeat


def main() -> None:
    f = input()
    print(" ".join(args := sorted({i for i in f if i.isupper()})) + " F")
    for i in product([0, 1], repeat=len(args)):
        print(*i, int(eval(f, dict(zip(args, i)))))


if __name__ == "__main__":
    main()
