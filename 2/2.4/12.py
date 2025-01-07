# Числовой прямоугольник
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))
    for i in range(1, n * m + 1):
        print(f"{i:>{width}} ", end=" " * (i % m == 0) + "\n" * (i % m == 0 and i != n * m))


if __name__ == "__main__":
    main()
