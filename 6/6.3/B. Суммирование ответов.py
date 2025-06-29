from requests import get


def main() -> None:
    address, result = f"http://{input()}", 0
    while number := int(get(address).text):
        result += number
    print(result)


if __name__ == "__main__":
    main()
