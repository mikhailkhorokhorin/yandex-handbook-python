# Украшение чека
def main():
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]
    print("=" * 16 + "Чек" + "=" * 16)
    print("Товар:" + f"{name:>29}")
    print("Цена:" + f"{f"{weight}кг * {coast}руб/кг":>30}")
    print("Итого:" + f"{f"{weight * coast}руб":>29}")
    print("Внесено:" + f"{f"{money}руб":>27}")
    print("Сдача:" + f"{f"{money - weight * coast}руб":>29}")
    print("=" * 35)


if __name__ == "__main__":
    main()
