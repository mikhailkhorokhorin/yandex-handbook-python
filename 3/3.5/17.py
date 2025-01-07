# Прятки
def main() -> None:
    with open("secret.txt", "r", encoding="UTF-8") as file:
        for symbol in file.read():
            print(chr(ord(symbol) % 128), end="")


if __name__ == "__main__":
    main()
