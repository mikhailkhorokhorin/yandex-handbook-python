def main() -> None:
    list = {}
    for i in range(int(input())):
        string = input().split()
        name, porridge = string[0], string[1:]
        for j in porridge:
            list.setdefault(j, []).append(name)
    print(*(sorted(list[n])), sep="\n") if (n := input()) in list else print("Таких нет")


if __name__ == "__main__":
    main()
