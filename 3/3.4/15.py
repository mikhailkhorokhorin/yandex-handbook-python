from itertools import permutations


def main():
    list = [x for _ in range(int(input())) for x in input().split(", ")]
    for a in permutations(sorted(list), 3):
        print(' '.join(a))


if __name__ == "__main__":
    main()
