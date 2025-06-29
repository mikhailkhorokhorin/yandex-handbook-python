def main() -> None:
    for _ in range(int(input())):
        print(
            string.index("зайка") + 1
            if "зайка" in (string := input())
            else "Заек нет =("
        )


if __name__ == "__main__":
    main()
