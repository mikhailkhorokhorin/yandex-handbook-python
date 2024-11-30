def main():
    strings = {}
    while (string := input()) != "":
        words = string.split()
        for word in words:
            word = word.upper()
            letter = word[(len(word) // 2) - 1] if len(word) % 2 == 0 else word[len(word) // 2]
            letter = letter.lower()

            if letter not in strings:
                strings[letter] = [word]
            else:
                strings[letter] += [word]

    for alpha, values in sorted(strings.items()):
        print(f"{alpha} \"{". ".join(sorted(set([_ for _ in values])))}\"")


if __name__ == "__main__":
    main()
