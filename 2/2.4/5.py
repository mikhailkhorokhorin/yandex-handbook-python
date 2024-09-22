def find():
    res = 0
    while (s := input()) != "ВСЁ":
        if s == "зайка":
            res = 1
    return res


def main():
    res = 0
    for x in range(int(input())):
        res += find()
    print(res)


if __name__ == "__main__":
    main()
