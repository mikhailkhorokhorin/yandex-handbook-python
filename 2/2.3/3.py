# Считалочка
def main() -> None:
    print(*[i for i in range(int(input()), int(input()) + 1)], end=" ")


if __name__ == "__main__":
    main()
