def main() -> None:
    alphabet = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
        "Ь": "",
        "Ъ": "",
    }
    for letter in input():
        if letter.upper() in "ЬЪ":
            continue
        elif letter.upper() in alphabet:
            if letter.isupper():
                print(
                    alphabet[letter][0].upper() + alphabet[letter][1:].lower(),
                    end="",
                )
            else:
                print(alphabet[letter.upper()].lower(), end="")
        else:
            print(letter, end="")


if __name__ == "__main__":
    main()
