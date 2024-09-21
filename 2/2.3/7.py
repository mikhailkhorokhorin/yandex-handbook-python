def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def main():
    a, b = [int(input()) for _ in range(2)]
    print(a * b // NOD(a, b))


if __name__ == "__main__":
    main()
