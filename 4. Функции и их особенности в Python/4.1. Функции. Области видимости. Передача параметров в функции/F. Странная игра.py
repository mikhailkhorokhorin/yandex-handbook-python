result = 0


def move(name: str, count: int) -> None:
    global result
    result += count if name == "Петя" else -count


def game_over() -> str:
    return "Петя" if result > 0 else "Ваня" if result < 0 else "Ничья"
