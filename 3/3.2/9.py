def main():
    words = []
    while (s := input()) != "":
        words.extend(s.split())
    for i in set(words):
        print(i, words.count(i))


if __name__ == "__main__":
    main()
