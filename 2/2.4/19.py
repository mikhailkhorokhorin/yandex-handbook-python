def main():
    n = int(input())
    width = len(str(round(n / 2)))
    for i in range(n):
        for j in range(n):
            print(f"{min(i + 1, n - i, j + 1, n - j):>{width}}", end=" ")
        print()


if __name__ == "__main__":
    main()
