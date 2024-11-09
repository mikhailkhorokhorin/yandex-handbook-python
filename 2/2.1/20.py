def main():
    n, m, k1, k2 = [int(input()) for _ in range(4)]

    x = (m * n - n * k2) // (k1 - k2)
    y = n - x
    print(x, y)


if __name__ == "__main__":
    main()
