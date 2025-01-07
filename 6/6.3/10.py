# Удаление данных
from requests import delete


def main() -> None:
    delete(f"http://{input()}/users/{input()}")


if __name__ == "__main__":
    main()
