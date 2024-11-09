def main():
    name = input()
    coast, weight, money = [int(input()) for _ in range(3)]

    final_coast = weight * coast
    print("================Чек================")
    print("Товар:" + f"{name:>29}")
    print("Цена:" + f"{f"{weight}кг * {coast}руб/кг":>30}")
    print("Итого:" + f"{f"{final_coast}руб":>29}")
    print("Внесено:" + f"{f"{money}руб":>27}")
    print("Сдача:" + f"{f"{money - final_coast}руб":>29}")
    print("=" * 35)


if __name__ == "__main__":
    main()
