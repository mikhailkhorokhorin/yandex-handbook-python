# Числовая змейка 2.0
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(n):
        print(" ".join(f"{j * n + (i + 1 if j % 2 == 0 else n - i):>{width}}" for j in range(m)))


if __name__ == "__main__":
    main()
