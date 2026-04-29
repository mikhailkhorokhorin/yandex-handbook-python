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
