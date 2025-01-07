# Простая задача 3.0
def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))


def main() -> None:
    print(sum([is_prime(int(input())) for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
