def order(*args):
    temp = in_stock
    COFFEE = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1},
    }

    for grade in args:
        for ingridient in COFFEE[grade]:
            if COFFEE[grade].get(ingridient, 0) > in_stock[ingridient]:
                break
        else:
            for ingridient in COFFEE[grade]:
                in_stock[ingridient] -= COFFEE[grade][ingridient]
            return grade

    if in_stock == temp:
        return "К сожалению, не можем предложить Вам напиток"
