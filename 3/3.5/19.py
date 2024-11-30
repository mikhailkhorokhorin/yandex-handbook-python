def main():
    shift = int(input())
    alp = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])
    with open("public.txt", encoding="UTF-8") as f:
        rec = f.read()
    list = [x.lower() for x in rec]
    res = [alp[(alp.find(x.lower()) + shift) % 26] if x in alp else x for x in list]
    for x in range(len(res)):
        if rec[x].isupper():
            res[x] = res[x].upper()
    with open("private.txt", "w", encoding="UTF-8") as f:
        print(''.join(x for x in res), file=f)


if __name__ == "__main__":
    main()
