def main():
    x, y = 0, 0
    xcord = {"ВОСТОК": 1, "ЗАПАД": -1}
    ycord = {"СЕВЕР": 1, "ЮГ": -1}

    while (s := input()) != "СТОП":
        val = int(input())
        if s in xcord.keys():
            x += val * xcord[s]
        else:
            y += val * ycord[s]
    print(y, x, sep="\n")


if __name__ == "__main__":
    main()
