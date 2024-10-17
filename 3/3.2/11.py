def main():
    surnames = [input() for _ in range(int(input()))]
    print(sum([surnames.count(i) for i in set(surnames) if surnames.count(i) != 1]))


if __name__ == "__main__":
    main()
