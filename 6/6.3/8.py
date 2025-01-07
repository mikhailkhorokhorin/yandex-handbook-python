# Регистрация нового пользователя
from requests import post
from json import dumps


def main() -> None:
    address = f"http://{input()}/users"
    post(address, data=dumps({"username": input(), "last_name": input(), "first_name": input(), "email": input()}))


if __name__ == "__main__":
    main()
