def main() -> None:
    name, number = [input() for _ in range(2)]
    print(f"Группа №{number[0]}.")
    print(f"{number[2]}. {name}.")
    print(f"Шкафчик: {number}.")
    print(f"Кроватка: {number[1]}.")


if __name__ == "__main__":
    main()
