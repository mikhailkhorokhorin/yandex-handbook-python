print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!")
print("Как дела?")
mood = input()
if mood == "хорошо":
    print("Я за вас рада!")
elif mood == "плохо":
    print("Всё наладится!")