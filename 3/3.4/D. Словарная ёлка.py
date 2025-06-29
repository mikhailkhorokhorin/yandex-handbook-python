from itertools import accumulate


def main() -> None:
    print(*[word for word in accumulate(map(lambda x: x + " ", input().split()))], sep='\n')


if __name__ == "__main__":
    main()
