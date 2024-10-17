def main():
    surnames = [input() for _ in range(int(input()))]
    namesakes = sorted(set([x for x in surnames if surnames.count(x) != 1]))

    if len(namesakes) == 0:
        print("Однофамильцев нет")
    else:
        for i in namesakes:
            print(f"{i} - {surnames.count(i)}")


if __name__ == "__main__":
    main()
