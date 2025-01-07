# Расклад таков...
from itertools import product, permutations


def main() -> None:
    raw_suit = input()
    suits = ["бубен", "пик", "треф", "червей"]
    best_suit = [x for x in suits if x[0] == raw_suit[0]][0]
    nominal = sorted([*[str(x) for x in range(2, 11)], "валет", "дама", "король", "туз"])
    nominal.remove(input())

    card_list = [f"{value} {suit}" for value, suit in product(nominal, suits)]
    card_layout_list = [", ".join(card_layout) for card_layout in product(card_list, repeat=3) if
                        len(set(card_layout)) == 3]
    print(*([card_layout for card_layout in card_layout_list if best_suit in card_layout][:10]), sep="\n")


if __name__ == "__main__":
    main()
