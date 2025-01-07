# Суммирование ответов 3
from requests import get
from sys import stdin


def main() -> None:
    address, ways = f"http://{input()}", [i.strip() for i in stdin]
    result = 0
    for way in ways:
        result += sum(get(address + way).json())
    print(result)


if __name__ == "__main__":
    main()
