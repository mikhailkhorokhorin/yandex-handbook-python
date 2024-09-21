def main():
    n, m = [int(input()) for _ in range(2)]

    p = 7 - 3 + 2 + n
    v = 6 + 3 + 5 - 2 + m

    print("Петя" if p > v else "Вася")


if __name__ == "__main__":
    main()
