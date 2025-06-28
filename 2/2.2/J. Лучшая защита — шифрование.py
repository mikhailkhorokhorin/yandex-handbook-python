def main() -> None:
    number = int(input())
    ind1 = number % 10 + (number // 10) % 10
    ind0 = number // 100 + (number // 10) % 10
    print(f"{ind1}{ind0}" if ind1 >= ind0 else f"{ind0}{ind1}")


if __name__ == "__main__":
    main()
