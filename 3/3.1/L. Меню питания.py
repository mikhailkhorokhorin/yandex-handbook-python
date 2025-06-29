def main() -> None:
    print(*[["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"][i % 5] for i in range(int(input()))], sep="\n")


if __name__ == "__main__":
    main()
