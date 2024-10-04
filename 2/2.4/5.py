def find():
    res = 0
    while (s := input()) != "ВСЁ":
        if s == "зайка":
            res = 1
    return res


def main():
    print(find() for x in range(int(input())))


if __name__ == "__main__":
    main()
