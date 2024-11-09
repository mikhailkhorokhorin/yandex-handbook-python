def main():
    products = [input() for _ in range(int(input()))]
    dishes = {}
    cancook = []
    for _ in range(int(input())):
        name = input()
        dishes[name] = [input() for _ in range(int(input()))]
        if len(set(dishes[name]) - set(products)) == 0:
            cancook.append(name)
    if len(cancook) == 0:
        print("Готовить нечего")
    else:
        print(*sorted(cancook), sep="\n")


if __name__ == "__main__":
    main()
