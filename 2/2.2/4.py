# Список победителей
def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(*[f"{i + 1}. {sorted_rating[i][0]}" for i in range(3)], sep="\n")


if __name__ == "__main__":
    main()
