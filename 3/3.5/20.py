# Файловая сумма
def main() -> None:
    with open("numbers.num", "rb") as file:
        numbers = file.read()
    print(sum([int.from_bytes(numbers[i:i + 2], "big") for i in range(0, len(numbers), 2)]) % 2 ** 16)


if __name__ == "__main__":
    main()
