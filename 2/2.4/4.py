def main():
    d = [input() for _ in range(int(input()))]
    print(sum([int(i) for x in d for i in x]))


if __name__ == "__main__":
    main()
