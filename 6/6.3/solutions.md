# Модуль requests

### Проверка системы

```python
from requests import get


def main() -> None:
    print(get("http://127.0.0.1:5000").text)


if __name__ == "__main__":
    main()
```

### Суммирование ответов

```python
from requests import get


def main() -> None:
    address, result = f"http://{input()}", 0
    while number := int(get(address).text):
        result += number
    print(result)


if __name__ == "__main__":
    main()
```

### Суммирование ответов 2

```python
from requests import get


def main() -> None:
    print(sum(i for i in get(f"http://{input()}").json() if isinstance(i, int)))


if __name__ == "__main__":
    main()
```

### Конкретное значение

```python
from requests import get


def main() -> None:
    address, key = f"http://{input()}", input()
    print(get(address).json().get(key, "No data"))


if __name__ == "__main__":
    main()
```

### Суммирование ответов 3

```python
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
```

### Список пользователей

```python
from requests import get


def main() -> None:
    address = f"http://{input()}/users"
    names = sorted(f"{user["last_name"]} {user["first_name"]}" for user in get(address).json())
    print("\n".join(names))


if __name__ == "__main__":
    main()
```

### Рассылка сообщений

```python
from requests import get
from sys import stdin


def main() -> None:
    address, text = f"http://{input()}/users/{input()}", "".join(i for i in stdin.read())
    try:
        print(text.format(**get(address).json()))
    except (ValueError, KeyError):
        print("Пользователь не найден")


if __name__ == "__main__":
    main()
```

### Регистрация нового пользователя

```python
from requests import post
from json import dumps


def main() -> None:
    address = f"http://{input()}/users"
    post(address, data=dumps({"username": input(), "last_name": input(), "first_name": input(), "email": input()}))


if __name__ == "__main__":
    main()
```

### Изменение данных

```python
from requests import put
from json import dumps
from sys import stdin


def main() -> None:
    address = f"http://{input()}/users/{input()}"
    put(address, data=dumps({line[0]: line[1] for line in (i.strip().split("=") for i in stdin)}))


if __name__ == "__main__":
    main()
```

### Удаление данных

```python
from requests import delete


def main() -> None:
    delete(f"http://{input()}/users/{input()}")


if __name__ == "__main__":
    main()
```