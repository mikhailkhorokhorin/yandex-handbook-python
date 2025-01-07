# Игра в «Угадайку»
def main() -> None:
    number, half = 500, 250
    print(number)
    while (string := input()) != "Угадал!":
        number += half if string == "Больше" else -half if string == "Меньше" else 0
        half = (half + 1) // 2 if half >= 2 else ...
        print(number)


if __name__ == "__main__":
    main()
