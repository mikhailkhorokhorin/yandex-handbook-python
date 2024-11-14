from itertools import product


def main():
    n = int(input())
    print("А Б В")
    for a1, a2, a3 in product(range(1, n + 1), repeat=3):
        print(a1, a2, a3) if a1 + a2 + a3 == n else ...


if __name__ == "__main__":
    main()
