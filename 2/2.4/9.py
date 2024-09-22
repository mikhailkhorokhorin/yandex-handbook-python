def main():
    d = [input() for _ in range(int(input()))]
    max_d = [max(int(i) for i in x) for x in d]
    print(*max_d, sep="")


if __name__ == "__main__":
    main()
