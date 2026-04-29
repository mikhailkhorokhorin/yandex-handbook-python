def GCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def main() -> None:
    numbers = [int(input()) for _ in range(int(input()))]
    gcd = 0
    for i in range(len(numbers)):
        gcd = GCD(gcd, numbers[i])
    print(gcd)


if __name__ == "__main__":
    main()
