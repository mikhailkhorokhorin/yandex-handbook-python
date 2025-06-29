from sys import stdin
import json


def main() -> None:
    user = [x.strip() for x in stdin]
    with open("scoring.json", encoding="UTF-8") as f:
        data = json.load(f)
    points = count = 0
    data = [{test["pattern"]: block["points"] // len(block["tests"]) for test in block["tests"]} for block in data]
    for i in data:
        for j in range(count, len(i) + count):
            if user[j] in i:
                points += i[user[j]]
            count += 1
    print(points)


if __name__ == "__main__":
    main()
