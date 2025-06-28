def find() -> int:
    founded = 0
    while (string := input()) != "ВСЁ":
        if string == "зайка":
            founded = 1
    return founded


def main() -> None:
    print(sum([find() for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
