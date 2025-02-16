# Транслитерация 2.0
def main() -> None:
    alphabet = {
        "А": "A", "Б": "B", "В": "V",
        "Г": "G", "Д": "D", "Е": "E",
        "Ё": "E", "Ж": "ZH", "З": "Z",
        "И": "I", "Й": "I", "К": "K",
        "Л": "L", "М": "M", "Н": "N",
        "О": "O", "П": "P", "Р": "R",
        "С": "S", "Т": "T", "У": "U",
        "Ф": "F", "Х": "KH", "Ц": "TC",
        "Ч": "CH", "Ш": "SH", "Щ": "SHCH",
        "Ы": "Y", "Э": "E", "Ю": "IU",
        "Я": "IA", "Ь": "", "Ъ": ""}
    data, translit_data = "", ""
    with open("cyrillic.txt", encoding="UTF-8") as file:
        for line in file:
            data += line

    for i in data:
        if i.upper() in alphabet:
            translit_data += alphabet[i.upper()].lower().capitalize() if i == i.upper() else alphabet[i.upper()].lower()
        else:
            translit_data += i

    with open("transliteration.txt", "w", encoding="UTF-8") as file:
        print(translit_data, file=file)


if __name__ == "__main__":
    main()
