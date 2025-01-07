# Территория зла
def main() -> None:
    side1, side2, c = [int(input()) for _ in range(3)]
    if (side1 ** 2 == side2 ** 2 + c ** 2) or (side2 ** 2 == side1 ** 2 + c ** 2) or (c ** 2 == side1 ** 2 + side2 ** 2):
        print("100%")
    elif (side1 ** 2 > side2 ** 2 + c ** 2) or (side2 ** 2 > side1 ** 2 + c ** 2) or (c ** 2 > side1 ** 2 + side2 ** 2):
        print("велика")
    else:
        print("крайне мала")


if __name__ == "__main__":
    main()
