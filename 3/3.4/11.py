def main():
    n, m = [int(input()) for _ in range(2)]
    cell = len(str(n * m))
    for a in range(1, n * m + 1):
        print(f"{a:>{cell}}", end=" " if a % m != 0 else "\n")


if __name__ == "__main__":
    main()
