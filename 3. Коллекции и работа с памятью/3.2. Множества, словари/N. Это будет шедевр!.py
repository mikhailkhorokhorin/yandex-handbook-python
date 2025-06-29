def main() -> None:
    products = [input() for _ in range(int(input()))]
    dishes, can_cook = {}, []
    for _ in range(int(input())):
        name = input()
        dishes[name] = [input() for _ in range(int(input()))]
        (
            can_cook.append(name)
            if len(set(dishes[name]) - set(products)) == 0
            else ...
        )
    (
        print(*sorted(can_cook), sep="\n")
        if can_cook
        else print("Готовить нечего")
    )


if __name__ == "__main__":
    main()
