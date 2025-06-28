def main() -> None:
    num1, num2 = [int(input()) for _ in range(2)]
    ind2 = (num1 // 100 + num2 // 100) % 10
    ind1 = ((num1 // 10) % 10 + (num2 // 10) % 10) % 10
    ind0 = (num1 % 10 + num2 % 10) % 10
    print(f"{ind2 * 100 + ind1 * 10 + ind0}")


if __name__ == "__main__":
    main()
