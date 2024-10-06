def f(n):
    return n * f(n - 1) if n > 1 else 1


def main():
    print(f(int(input())))


if __name__ == "__main__":
    main()
