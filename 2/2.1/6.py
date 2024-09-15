name = input()
coast = int(input())
weight = int(input())
money = int(input())

final_coast = weight * coast
print("Чек")
print(f"{name} - {weight}кг - {coast}руб/кг")
print(f"Итого: {final_coast}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - final_coast}руб")