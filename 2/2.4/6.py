def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def main():
    d = [int(input()) for _ in range(int(input()))]
    nod = 0
    for i in range(len(d)):
        nod = NOD(nod, d[i])
    print(nod)


if __name__ == "__main__":
    main()
