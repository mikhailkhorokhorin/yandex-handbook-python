# Суммарная сумма
def main() -> None:
    print(sum([int(i) for x in [input() for _ in range(int(input()))] for i in x]))


if __name__ == "__main__":
    main()
