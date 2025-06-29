def is_prime(num: int) -> bool:
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def main() -> None:
    print("YES" if is_prime(int(input())) else "NO")


if __name__ == "__main__":
    main()
