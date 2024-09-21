def main():
    name = input("Как Вас зовут?\n")
    print(f"Здравствуйте, {name}!")
    mood = input("Как дела?\n")

    print("Я за вас рада!" if mood == "хорошо" else "Всё наладится!")


if __name__ == "__main__":
    main()
