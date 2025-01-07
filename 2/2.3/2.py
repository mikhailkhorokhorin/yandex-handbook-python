# Зайка — 3
def main() -> None:
    count = 0
    while (string := input()) != "Приехали!":
        count += 1 if "зайка" in string else ...
    print(count)


if __name__ == "__main__":
    main()
