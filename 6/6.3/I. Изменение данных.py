from requests import put
from json import dumps
from sys import stdin


def main() -> None:
    address = f"http://{input()}/users/{input()}"
    put(address, data=dumps({line[0]: line[1] for line in (i.strip().split("=") for i in stdin)}))


if __name__ == "__main__":
    main()
