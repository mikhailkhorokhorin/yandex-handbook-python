# Числовая змейка
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(" ".join(f"{i * m + (j + 1 if i % 2 == 0 else m - j):>{width}}" for j in range(m)))


if __name__ == "__main__":
    main()
