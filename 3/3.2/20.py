def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def main():
    line = sorted(set(map(int, input().split("; "))))
    res = {str(i): [] for i in line}
    for i in line:
        for j in line:
            if i != j and NOD(i, j) == 1:
                res[str(i)].extend([str(j)])
        if len(res[str(i)]):
            print(f"{i} - ", end="")
            print(", ".join(res[str(i)]))


if __name__ == "__main__":
    main()
