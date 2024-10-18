from itertools import product


def main():
    n = int(input())
    for i in range(n):
        for j in range(i):
            print(j + i + 1, end=" ")


if __name__ == "__main__":
    main()
