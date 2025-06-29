from requests import get
from sys import stdin


def main() -> None:
    address, text = f"http://{input()}/users/{input()}", "".join(
        i for i in stdin.read()
    )
    try:
        print(text.format(**get(address).json()))
    except (ValueError, KeyError):
        print("Пользователь не найден")


if __name__ == "__main__":
    main()
