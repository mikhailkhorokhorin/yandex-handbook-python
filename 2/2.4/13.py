def main():
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(1, n + 1):
        num = i
        for _ in range(m):
            print(f"{num:>{width}}", end=" ")
            num += n
        print()


if __name__ == "__main__":
    main()
