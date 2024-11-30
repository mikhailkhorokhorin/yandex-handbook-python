import json
from sys import stdin


def main():
    file = input()
    with open(file, encoding="UTF-8") as f:
        data = json.load(f)
    for line in stdin:
        before = line[:line.find('=')].rstrip()
        after = line[line.find('==') + 2:].lstrip()
        data[before] = after.rstrip()
    with open(file, "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
