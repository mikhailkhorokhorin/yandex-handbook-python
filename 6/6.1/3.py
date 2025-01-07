# Есть варианты?
from math import comb


def main() -> None:
    n, m = map(int, input().split())
    print(comb(n, m) * m // n, comb(n, m))


if __name__ == "__main__":
    main()
