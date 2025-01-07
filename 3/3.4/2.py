# Сборы на прогулку
def main() -> None:
    names1, names2 = [input().split(", ") for _ in range(2)]
    print(*[f"{names1[i]} - {names2[i]}" for i in range(min(len(names1), len(names2)))], sep="\n")


if __name__ == "__main__":
    main()
