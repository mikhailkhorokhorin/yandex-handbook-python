from itertools import permutations


def main():
    n = int(input())
    for a in permutations(sorted([input() for _ in range(n)])):
        print(', '.join(a))


if __name__ == "__main__":
    main()
