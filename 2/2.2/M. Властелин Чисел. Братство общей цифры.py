def main() -> None:
    num1, num2, num3 = [int(input()) for _ in range(3)]
    print(num1 // 10 if (num1 // 10) == (num2 // 10) == (num3 // 10) else num1 % 10)


if __name__ == "__main__":
    main()
