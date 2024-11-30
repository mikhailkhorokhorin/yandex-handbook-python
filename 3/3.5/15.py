from sys import stdin
import json


def main():
    ans = [x.strip() for x in stdin]
    with open("scoring.json", encoding="UTF-8") as f:
        data = json.load(f)
    sum = num = 0
    data = [{test["pattern"]: block["points"] // len(block["tests"]) for test in block["tests"]} for block in data]
    for i in data:
        for j in range(num, len(i) + num):
            if ans[j] in i:
                sum += i[ans[j]]
            num += 1
    print(sum)


if __name__ == "__main__":
    main()
