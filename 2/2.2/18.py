def main():
    a, b, c = [int(input()) for _ in range(3)]

    if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
        print("100%")
    elif (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2) or (c ** 2 > a ** 2 + b ** 2):
        print("велика")
    else:
        print("крайне мала")


if __name__ == "__main__":
    main()
