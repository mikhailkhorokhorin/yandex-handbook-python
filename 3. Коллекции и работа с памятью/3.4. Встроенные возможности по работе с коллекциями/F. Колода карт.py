def main() -> None:
    deck, suit = [
        (x, y)
        for x in [*[i for i in range(2, 11)], "валет", "дама", "король", "туз"]
        for y in ["пик", "треф", "бубен", "червей"]
    ], input()
    print(*[f"{x} {y}" for x, y in deck if y != suit], sep="\n")


if __name__ == "__main__":
    main()
