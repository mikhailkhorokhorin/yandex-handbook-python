# Таблица умножения 3.0
from itertools import product


def main() -> None:
    n = int(input())
    for a1, a2 in product(range(1, n + 1), repeat=2):
        print(a1 * a2, end=" ")
        if a2 == n:
            print()


if __name__ == "__main__":
    main()

