def main() -> None:
    string = input()
    print(*[string for _ in range(3)], sep="\n")


if __name__ == "__main__":
    main()
