def main() -> None:
    num1, num2 = [int(input()) for _ in range(2)]
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    print(num1 + num2)


if __name__ == "__main__":
    main()
