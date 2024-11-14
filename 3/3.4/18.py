from itertools import product


def main():
    print("a b c f")
    s = input()
    for a, b, c in product([0, 1], repeat=3):
        print(a, b, c, int(eval(s)))


if __name__ == "__main__":
    main()
