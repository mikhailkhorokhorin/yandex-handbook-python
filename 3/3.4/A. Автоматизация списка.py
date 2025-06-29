def main() -> None:
    line = input()
    print(*[f"{line.split().index(word) + 1}. {word}" for word in line.split()], sep="\n")


if __name__ == "__main__":
    main()
