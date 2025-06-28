def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]
    print(sorted_rating[0][0])


if __name__ == "__main__":
    main()
