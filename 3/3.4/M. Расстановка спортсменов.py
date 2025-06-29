from itertools import permutations


def main() -> None:
    print("\n".join(", ".join(a) for a in permutations(sorted([input() for _ in range(int(input()))]))))


if __name__ == "__main__":
    main()
