def main():
    porridges = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
    for i in range(int(input())):
        print(porridges[i % 5])


if __name__ == "__main__":
    main()
