# Хвост
def main() -> None:
    f, n = input(), int(input())
    data = []
    with open(f, "r") as f:
        for line in f:
            data.append(line)
    for line in data[-n:]:
        print(line.strip())


if __name__ == "__main__":
    main()
