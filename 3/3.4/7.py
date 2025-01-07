# Игровая сетка
from itertools import combinations


def main() -> None:
    print(*[f"{x} - {y}" for x, y in combinations([input() for _ in range(int(input()))], 2)], sep="\n")


if __name__ == "__main__":
    main()
