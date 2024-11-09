def main():
    n, m = [int(input()) for _ in range(2)]
    names = [input() for _ in range(n + m)]
    names = [i for i in names if names.count(i) == 1]
    print(*(sorted(names)), sep="\n") if len(names) else print("Таких нет")


if __name__ == "__main__":
    main()
