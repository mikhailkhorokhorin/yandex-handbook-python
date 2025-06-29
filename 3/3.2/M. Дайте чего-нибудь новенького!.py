def main() -> None:
    menu = [input() for _ in range(int(input()))]
    cooked = []
    for _ in range(int(input())):
        cooked.extend([input() for _ in range(int(input()))])
    print(*other, sep="\n") if (other := sorted(set(menu) - set(cooked))) else print("Готовить нечего")


if __name__ == "__main__":
    main()
