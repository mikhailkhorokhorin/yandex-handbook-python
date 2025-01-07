# Максимальная сумма
def main() -> None:
    rating = {}
    for _ in range(int(input())):
        name = input()
        rating[name] = sum([int(x) for x in input()])
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(sorted_rating[0][0])


if __name__ == "__main__":
    main()
