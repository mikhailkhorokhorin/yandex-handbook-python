# Простая задача 2.0
def main() -> None:
    number, multipliers, divider = int(input()), [], 2
    print(number) if number < 2 else ...

    while number > 1:
        if number % divider == 0:
            multipliers.append(divider)
            number //= divider
        else:
            divider += 1

    print(*multipliers, sep=" * ")


if __name__ == "__main__":
    main()
