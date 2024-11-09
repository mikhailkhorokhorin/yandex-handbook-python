def main():
    list = {}
    for i in range(int(input())):
        string = input().split()
        name, porridge = string[0], string[1:]
        for j in porridge:
            if j not in list:
                list[j] = [name]
            else:
                list[j] += [name]
    n = input()
    print(*(sorted(list[n])), sep="\n") if n in list else print("Таких нет")


if __name__ == "__main__":
    main()
