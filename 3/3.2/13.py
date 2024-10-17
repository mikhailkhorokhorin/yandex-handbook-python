def main():
    menu = [input() for _ in range(int(input()))]
    cooked = []
    for _ in range(int(input())):
        cooked.extend([input() for _ in range(int(input()))])
    other = sorted(set(menu) - set(cooked))
    if len(other) == 0:
        print("Готовить нечего")
    print(*other, sep="\n")


if __name__ == "__main__":
    main()
