def main():
    n, m = [int(input()) for _ in range(2)]
    semolina = set([input() for _ in range(n)])
    oatmeal = set([input() for _ in range(m)])
    both = semolina & oatmeal
    print(len(both) if len(both) else "Таких нет")


if __name__ == "__main__":
    main()
