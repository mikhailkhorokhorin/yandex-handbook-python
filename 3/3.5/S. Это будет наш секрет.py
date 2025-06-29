def main() -> None:
    shift = int(input())
    alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
    with open("public.txt", encoding="UTF-8") as file:
        data = file.read()
    words = [x.lower() for x in data]
    res = [alphabet[(alphabet.find(x.lower()) + shift) % 26] if x in alphabet else x for x in words]
    for x in range(len(res)):
        if data[x].isupper():
            res[x] = res[x].upper()
    with open("private.txt", "w", encoding="UTF-8") as file:
        print(''.join(x for x in res), file=file)


if __name__ == "__main__":
    main()
