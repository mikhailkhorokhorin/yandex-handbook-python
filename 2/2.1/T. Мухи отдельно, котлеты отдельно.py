def main() -> None:
    n, m, k1, k2 = [int(input()) for _ in range(4)]
    batch1 = (m * n - n * k2) // (k1 - k2)
    batch2 = n - batch1
    print(batch1, batch2)


if __name__ == "__main__":
    main()
