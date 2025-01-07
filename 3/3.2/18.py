# Карта сокровищ
def main() -> None:
    result = {}
    for _ in range(int(input())):
        cords = input().split()
        x = f'{cords[0][:-1]}-{cords[1][:-1]}'
        result[x] = result.get(x, 0) + 1
    print(max(result.values()))


if __name__ == "__main__":
    main()
