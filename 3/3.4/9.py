from itertools import product


def main():
    n, k = int(input()), 0
    for a1, a2 in product(range(1, n + 1), repeat=2):
        print(a1 * a2, end=" ")
        k += 1
        if k == n:
            print()
            k = 0


if __name__ == "__main__":
    main()
