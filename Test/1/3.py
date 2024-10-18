def main():
    m, n = [int(input()) for _ in range(2)]
    print(", ".join([str(x) for x in range(n, m + 1, (n - m) % 10)]))


if __name__ == "__main__":
    main()
