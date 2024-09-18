x = float(input())
y = float(input())

rectangle = -4 <= x <= 0 and 0 <= y <= 5
circle = x >= 0 and y >= 0 and x ** 2 + y ** 2 <= 25
parable = y <= 0 and 0.25 * (x - 1) ** 2 - 9 <= y


def triangle(x, y, x1, y1, x2, y2, x3, y3):
    alltr = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))

    subtr1 = 0.5 * abs((x - x1) * (y2 - y1) - (x2 - x1) * (y - y1))
    subtr2 = 0.5 * abs((x - x2) * (y3 - y2) - (x3 - x2) * (y - y2))
    subtr3 = 0.5 * abs((x - x3) * (y1 - y3) - (x1 - x3) * (y - y3))
    return alltr == subtr1 + subtr2 + subtr3


if (x ** 2 + y ** 2 > 100):
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif (rectangle or circle or parable or triangle(x, y, -7, 0, -4, 5, -4, 0)):
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")
