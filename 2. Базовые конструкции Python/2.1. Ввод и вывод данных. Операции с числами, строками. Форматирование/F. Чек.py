def main() -> None:
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]
    print("Чек")
    print(f"{name} - {weight}кг - {coast}руб/кг")
    print(f"Итого: {weight * coast}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - weight * coast}руб")


if __name__ == "__main__":
    main()
