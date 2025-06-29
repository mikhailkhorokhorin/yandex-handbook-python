def main() -> None:
    surnames = [input() for _ in range(int(input()))]
    namesakes = sorted(set([x for x in surnames if surnames.count(x) != 1]))
    print(*[f"{i} - {surnames.count(i)}" for i in namesakes], sep="\n") if namesakes else print("Однофамильцев нет")


if __name__ == "__main__":
    main()
