def main():
    x, y = [float(input()) for _ in range(2)]

    rectangle = y <= 5
    circle = x ** 2 + y ** 2 <= 25
    parable = y >= 0.25 * (x + 1) ** 2 - 9
    triangle = y <= (5 / 3) * x + (35 / 3)

    if (rectangle and circle and parable and triangle):
        print("Опасность! Покиньте зону как можно скорее!")
    elif (x ** 2 + y ** 2 >= 100):
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")


if __name__ == "__main__":
    main()
