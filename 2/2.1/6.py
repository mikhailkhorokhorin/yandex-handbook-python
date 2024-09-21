def main():
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]
    final_coast = weight * coast

    print("Чек")
    print(f"{name} - {weight}кг - {coast}руб/кг")
    print(f"Итого: {final_coast}руб")
    print(f"Внесено: {money}руб")
    print(f"Сдача: {money - final_coast}руб")


if __name__ == "__main__":
    main()
