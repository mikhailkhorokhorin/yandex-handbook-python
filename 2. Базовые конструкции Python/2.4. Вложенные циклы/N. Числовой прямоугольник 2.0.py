def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(" ".join(f"{i + 1 + j * n:>{width}}" for j in range(m)))


if __name__ == "__main__":
    main()
