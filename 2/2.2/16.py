# Легенды велогонок возвращаются: кто быстрее?
def main() -> None:
    rating = {"Петя": int(input()), "Вася": int(input()), "Толя": int(input())}
    sorted_rating = sorted(rating.items(), key=lambda x: x[1])[::-1]

    print(f"{f"{sorted_rating[0][0]}":^24}")
    print(f"{f"{sorted_rating[1][0]}":^8}")
    print(" " * 16 + f"{f"{sorted_rating[2][0]}":^8}")
    print(f"{"II":^8}" + f"{"I":^8}" + f"{"III":^8}")


if __name__ == "__main__":
    main()
