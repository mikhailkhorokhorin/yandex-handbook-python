def main():
    names = [input() for _ in range(int(input()))]
    table = []
    for i in range(len(names)):
        for j in range(i, len(names)):
            if i != j:
                table.append((names[i], names[j]))
    print(*[f"{x} - {y}" for x, y in table], sep="\n")


if __name__ == "__main__":
    main()
