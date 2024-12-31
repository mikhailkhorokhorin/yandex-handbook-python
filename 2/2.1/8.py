# Наказание
def main():
    n, message = int(input()), input()
    print(*[f"Я больше никогда не буду писать \"{message}\"!" for _ in range(n)], sep="\n")


if __name__ == "__main__":
    main()
