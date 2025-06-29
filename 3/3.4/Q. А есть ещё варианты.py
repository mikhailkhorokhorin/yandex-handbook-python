from itertools import product, permutations


def main() -> None:
    raw_suit = input()
    suits = ["бубен", "пик", "треф", "червей"]
    best_suit = [x for x in suits if x[0] == raw_suit[0]][0]
    nominal = sorted(
        [*[str(x) for x in range(2, 11)], "валет", "дама", "король", "туз"]
    )
    nominal.remove(input())

    card_layout_tuple = tuple(permutations(product(nominal, suits), r=3))
    card_layout_tuple = (
        ", ".join(" ".join(card_tuple) for card_tuple in sorted(card_layout))
        for card_layout in card_layout_tuple
    )
    card_layout_list = [
        card_layout
        for card_layout in sorted(set(card_layout_tuple))
        if best_suit in card_layout
    ]
    print(card_layout_list[card_layout_list.index(input()) + 1])


if __name__ == "__main__":
    main()
