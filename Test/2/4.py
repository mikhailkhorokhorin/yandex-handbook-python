from itertools import permutations


def main():
    string = sorted(set(input().split("; ")))
    n = int(input())
    for p in permutations(string, r=n):
        print(*p, sep="")


if __name__ == "__main__":
    main()
