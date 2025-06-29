import json
from sys import stdin


def main() -> None:
    with open(user := input(), encoding="UTF-8") as file:
        data = json.load(file)
    for line in stdin:
        before = line[:line.find("=")].rstrip()
        after = line[line.find("==") + 2:].lstrip()
        data[before] = after.rstrip()
    with open(user, "w", encoding="UTF-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
