from sys import stdin


def clear(string: str) -> str:
    string = string.replace("\n", " ")
    while "  " in string:
        string = string.replace("  ", " ")
    return string


def main() -> None:
    string, flag = input(), True
    files = [x.strip() for x in stdin]
    for name in files:
        with open(name, encoding="UTF-8") as file:
            data = "".join(file.readlines()).lower()
            if string.lower() in clear(data):
                print(name)
                flag = False
    print("404. Not Found") if flag else ...


if __name__ == "__main__":
    main()
