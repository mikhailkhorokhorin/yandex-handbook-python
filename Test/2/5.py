from sys import stdin
import json


def main():
    d = []
    for x in stdin:
        d.append(x.lower().rstrip())
    print(d)
    alp = sorted(set([char for word in d for char in word if (char in word and word.index(char) % 2 != 0)]))
    result = dict.fromkeys(alp, [])
    for x in result.keys():
        result[x] = [i for i in d if x in i]

    print(result)
    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
