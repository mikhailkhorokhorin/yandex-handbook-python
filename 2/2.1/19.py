name = input()
coast = int(input())
weight = int(input())
money = int(input())

final_coast = weight * coast
print("================Чек================")
print("Товар:" + "{:>29}".format(name))
print("Цена:" + "{:>30}".format(f"{weight}кг * {coast}руб/кг"))
print("Итого:" + "{:>29}".format(f"{final_coast}руб"))
print("Внесено:" + "{:>27}".format(f"{money}руб"))
print("Сдача:" + "{:>29}".format(f"{money - final_coast}руб"))
print("===================================")
