def f(n):
    if n == 0:
        return 1
    return n * f(n - 1)


def main():
    print(f(int(input())))


if __name__ == "__main__":
    main()
