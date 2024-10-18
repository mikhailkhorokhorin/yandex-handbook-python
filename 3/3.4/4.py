from itertools import accumulate


def main():
    print(*[x for x in accumulate(map(lambda x: x + " ", input().split()))], sep='\n')


if __name__ == "__main__":
    main()
