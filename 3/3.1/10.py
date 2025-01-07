# Частотный анализ на минималках
def main() -> None:
    res = ""
    while (s := input()) != 'ФИНИШ':
        res += s
    line = str(res).lower().replace(" ", "")
    count, letter = 0, ""
    for char in set(line):
        if line.count(char) > count:
            letter, count = char, line.count(char)
    print(letter)


if __name__ == "__main__":
    main()
