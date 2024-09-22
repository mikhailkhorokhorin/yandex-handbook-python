def P(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def main():
    print(sum([P(int(input())) for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
