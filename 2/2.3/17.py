def main():
    num = input()
    res = [int(x) for x in num if int(x) % 2 != 0]
    print(*res, sep="")


if __name__ == "__main__":
    main()
