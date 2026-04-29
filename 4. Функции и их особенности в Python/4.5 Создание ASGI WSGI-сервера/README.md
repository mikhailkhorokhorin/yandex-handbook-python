# 4.5 Создание ASGI WSGI-сервера
### A. WSGI-сервер как функция
```python
import sys


def home_handler(params):
    return 200, "Home Page"


def admin_handler(params):
    return 200, "Admin Panel"


def user_handler(params):
    return 200, f"Hello, {params['name']}!"


def attempt_handler(params):
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params['task']}' is accepted!",
    )


def not_found_handler(params):
    return 404, "Not Found"


def router(path):
    if path == "/":
        return home_handler
    if path.startswith("/user"):
        return user_handler
    if path.startswith("/attempt"):
        return attempt_handler
    if path.startswith("/admin"):
        return admin_handler
    return not_found_handler


def wsgi_server():
    request = yield None
    while True:
        clean_req = request.strip().split(" ")[1]
        handler = router(clean_req)
        params = {}
        if "?" in clean_req:
            params = dict(
                pair.split("=") for pair in clean_req.split("?")[1].split("&")
            )
        response = handler(params)
        request = yield response


def main() -> None:
    app = wsgi_server()
    app.send(None)
    for request in sys.stdin:
        print(app.send(request))


if __name__ == "__main__":
    main()
```
### B. Middleware-декораторы
```python
import sys
from functools import wraps
from json import dumps


def require_auth(func):
    @wraps(func)
    def wrapper(args):
        if "name" not in args:
            return 403, "Forbidden"
        return func(args)

    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(args):
        func_name = func.__name__
        response = func(args)
        log = {"handler": func_name, "params": args, "response": [*response]}
        print(dumps(log))

    return wrapper


@log_call
def home_handler(params):
    return 200, "Home Page"


@log_call
def admin_handler(params):
    return 200, "Admin Panel"


@log_call
@require_auth
def user_handler(params):
    return 200, f"Hello, {params['name']}!"


@log_call
@require_auth
def attempt_handler(params):
    return (
        200,
        f"Good try, {params['name']}! Your attempt on task '{params['task']}' is accepted!",
    )


@log_call
def not_found_handler(params):
    return 404, "Not Found"


def router(path):
    if path == "/":
        return home_handler
    if path.startswith("/user"):
        return user_handler
    if path.startswith("/attempt"):
        return attempt_handler
    if path.startswith("/admin"):
        return admin_handler
    return not_found_handler


def wsgi_server():
    request = yield None
    while True:
        clean_req = request.strip().split(" ")[1]
        handler = router(clean_req)
        params = {}
        if "?" in clean_req:
            query = clean_req.split("?")[1]
            params = dict(pair.split("=") for pair in query.split("&"))

        response = handler(params)
        request = yield response


def main() -> None:
    app = wsgi_server()
    app.send(None)
    for request in sys.stdin:
        app.send(request)


if __name__ == "__main__":
    main()
```
### C. Аналитика решения задач пользователями
```python
from json import loads


def main() -> None:
    with open("app.log", "r", encoding="utf-8") as f:
        lines = f.readlines()

    lines_dict = map(lambda line: loads(line), lines)

    unique_users = set()
    popularity_tasks = dict()

    for data in lines_dict:
        if data["handler"] == "attempt_handler" and data["response"][0] == 200:
            params = data["params"]
            unique_users.add(params["name"])
            popularity_tasks[params["task"]] = (
                popularity_tasks.get(params["task"], 0) + 1
            )

    sorted_pop_tasks = sorted(popularity_tasks.items())
    max_populatity_taks = max(popularity_tasks.items(), key=lambda x: x[1])
    print("Analytics Results:")
    print(f"Unique users who solved tasks: {len(unique_users)}")
    print(f"Unique users list: {', '.join(sorted([*unique_users]))}")
    print(f"Task popularity: { {key: val for key, val in sorted_pop_tasks} }")
    print(
        f"Most popular task: '{max_populatity_taks[0]}' with {max_populatity_taks[1]} attempts"
    )


if __name__ == "__main__":
    main()
```
