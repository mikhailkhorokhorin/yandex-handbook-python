# Потоковый НОД
from math import gcd
from sys import stdin


def main() -> None:
    print(*[gcd(*map(int, i.split())) for i in stdin], sep="\n")


if __name__ == "__main__":
    main()
