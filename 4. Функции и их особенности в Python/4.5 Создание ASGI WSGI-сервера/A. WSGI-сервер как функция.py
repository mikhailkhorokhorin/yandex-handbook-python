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
