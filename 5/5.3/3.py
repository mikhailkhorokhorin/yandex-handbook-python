# Ломать — не строить 2
class Error:
    def __repr__(self):
        raise ValueError


try:
    func(Error())
except ValueError:
    print("Ура! Ошибка!")
