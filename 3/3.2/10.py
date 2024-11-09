def main():
    alphabet = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
        'Я': 'IA', 'Ь': '', 'Ъ': '',
    }
    for i in input():
        if i.upper() in "ЬЪ":
            continue
        elif i.upper() in alphabet:
            if i.isupper():
                print(alphabet[i][0].upper() + alphabet[i][1:].lower(), end="")
            else:
                print(alphabet[i.upper()].lower(), end="")
        else:
            print(i, end="")


if __name__ == "__main__":
    main()
