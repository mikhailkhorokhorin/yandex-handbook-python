from itertools import permutations


def main() -> None:
    for products in permutations(
        sorted([x for _ in range(int(input())) for x in input().split(", ")]), 3
    ):
        print(*[" ".join(products)])


if __name__ == "__main__":
    main()
