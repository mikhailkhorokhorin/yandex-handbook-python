def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    semolina = set([input() for _ in range(n)])
    oatmeal = set([input() for _ in range(m)])
    print(len(both) if len(both := (semolina & oatmeal)) else "Таких нет")


if __name__ == "__main__":
    main()
