def main() -> None:
    n = int(input())
    width = len(str(n // 2 + 1))
    for i in range(n):
        print(
            " ".join(
                f"{min(i + 1, n - i, j + 1, n - j):>{width}}" for j in range(n)
            )
        )


if __name__ == "__main__":
    main()
