def main() -> None:
    products = [x for _ in range(int(input())) for x in input().split(", ")]
    print(*[f"{index}. {element}" for index, element in enumerate(sorted(products), start=1)], sep="\n")


if __name__ == "__main__":
    main()
