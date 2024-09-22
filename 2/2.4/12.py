def main():
    n, m = [int(input()) for _ in range(2)]
    num = 0
    width = len(str(n * m))
    for _ in range(n):
        for _ in range(m):
            num += 1
            print(f"{num:>{width}}", end=" ")
        print()


if __name__ == "__main__":
    main()
