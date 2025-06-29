def main() -> None:
    words = []
    while (string := input()) != "":
        words.extend(string.split())
    print(*[f"{word} {words.count(word)}" for word in set(words)], sep="\n")


if __name__ == "__main__":
    main()
