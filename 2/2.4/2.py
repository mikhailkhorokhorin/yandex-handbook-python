# Не таблица умножения
def main() -> None:
    for i in range(1, (n := int(input())) + 1):
        print("\n".join(f"{j} * {i} = {i * j}" for j in range(1, n + 1)))


if __name__ == "__main__":
    main()
