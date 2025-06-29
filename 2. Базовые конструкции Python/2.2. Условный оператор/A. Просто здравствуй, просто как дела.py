def main() -> None:
    print(f"Здравствуйте, {input("Как Вас зовут?\n")}!")
    print(
        "Я за вас рада!"
        if input("Как дела?\n") == "хорошо"
        else "Всё наладится!"
    )


if __name__ == "__main__":
    main()
