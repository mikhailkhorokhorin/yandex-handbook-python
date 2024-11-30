from sys import stdin


def clear(x: str) -> str:
    x = x.replace('\n', ' ')
    while '  ' in x:
        x = x.replace('  ', ' ')
    return x


def main():
    string, flag = input(), True
    list = [x.strip() for x in stdin]
    for name in list:
        with open(name, encoding="UTF-8") as f:
            data = ''.join(f.readlines()).lower()
            if string.lower() in clear(data):
                print(name)
                flag = False
    print("404. Not Found") if flag else ...


if __name__ == "__main__":
    main()
