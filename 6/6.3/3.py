# Суммирование ответов 2
from requests import get


def main() -> None:
    print(sum(i for i in get(f"http://{input()}").json() if isinstance(i, int)))


if __name__ == "__main__":
    main()
