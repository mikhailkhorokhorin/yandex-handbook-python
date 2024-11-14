from itertools import product, repeat


def main():
    s = input()
    args = sorted({i for i in s if i.isupper()})
    print(" ".join(args) + " F")
    for i in product([0, 1], repeat=len(args)):
        x = locals()
        for j in range(len(args)):
            x[args[j]] = i[j]
        print(*i, int(eval(s)))


if __name__ == "__main__":
    main()
