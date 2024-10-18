from itertools import product


def main():
    s = input().replace("->","<=").replace("~","==")
    print(s)
    for A,B,C, in product([0,1], repeat = 3):
        print(A,B,C,exec(s))


if __name__ == "__main__":
    main()