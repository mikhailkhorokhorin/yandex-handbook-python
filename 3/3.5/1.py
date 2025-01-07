# A+B+...
from sys import stdin


def main() -> None:
    print(sum(map(int, stdin.read().split())))


if __name__ == "__main__":
    main()
