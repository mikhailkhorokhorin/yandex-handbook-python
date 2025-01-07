# Анонс новости 2.0
def main() -> None:
    length, strings = int(input()), [input() for _ in range(int(input()))]
    total = length
    for i in strings:
        if total <= 3:
            break
        print(i[:total:] if (total - len(i)) > 3 else i[:total - 3:] + "...")
        total -= len(i)


if __name__ == "__main__":
    main()
