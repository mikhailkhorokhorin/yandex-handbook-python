def main() -> None:
    candies, in_bag = [int(input()) for _ in range(2)]
    print(in_bag // candies, in_bag % candies, sep="\n")


if __name__ == "__main__":
    main()
