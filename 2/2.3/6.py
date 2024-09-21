def main():
    a, b = [int(input()) for _ in range(2)]

    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    print(a + b)


if __name__ == "__main__":
    main()
