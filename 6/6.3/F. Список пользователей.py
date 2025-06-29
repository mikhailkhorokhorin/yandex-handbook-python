from requests import get


def main() -> None:
    address = f"http://{input()}/users"
    names = sorted(f"{user["last_name"]} {user["first_name"]}" for user in get(address).json())
    print("\n".join(names))


if __name__ == "__main__":
    main()
