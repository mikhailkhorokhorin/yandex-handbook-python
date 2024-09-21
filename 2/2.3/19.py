def main():
    number = 500
    delta = 250

    print(number)
    while (s := input()) != "Угадал!":
        if s == "Меньше":
            number -= delta
        elif s == "Больше":
            number += delta
        if delta >= 2:
            delta = (delta + 1) // 2
        print(number)


if __name__ == "__main__":
    main()
