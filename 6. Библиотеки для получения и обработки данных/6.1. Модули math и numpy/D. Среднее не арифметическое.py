from math import pow, prod


def main() -> None:
    numbers = list(map(float, input().split()))
    print(pow(prod(numbers), 1 / len(numbers)))


if __name__ == "__main__":
    main()
