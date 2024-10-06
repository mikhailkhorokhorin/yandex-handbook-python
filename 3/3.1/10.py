def main():
    res = ""
    while (s := input()) != 'ФИНИШ':
        res += s
    line = str(res).lower().replace(" ", "")
    m, letter = 0, ""

    for i in set(line):
        if line.count(i) > m:
            letter = i
            m = line.count(i)
    print(letter)


if __name__ == "__main__":
    main()
