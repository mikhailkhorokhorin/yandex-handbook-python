def main() -> None:
    x = y = 0
    x_dir = {"ВОСТОК": 1, "ЗАПАД": -1}
    y_dir = {"СЕВЕР": 1, "ЮГ": -1}

    while (direction := input()) != "СТОП":
        value = int(input())
        (x, y) = (
            (x + value * x_dir[direction], y)
            if direction in x_dir
            else (x, y + value * y_dir[direction])
        )
    print(y, x, sep="\n")


if __name__ == "__main__":
    main()
