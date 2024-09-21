def main():
    num = 500
    k = 250

    print(num)
    while (s := input()) != "Угадал!":
        if s == "Меньше":
            num -= k
        elif s == "Больше":
            num += k
        if k >= 2:
            k = (k + 1) // 2
        print(num)


if __name__ == "__main__":
    main()
