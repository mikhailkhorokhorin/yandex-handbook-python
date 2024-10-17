def div(x):
    return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in (d, x // d)})


def main():
    string = list(map(int, input().split("; ")))
    for i in string:
        res = set(string) - set(div(i))
        print(f"{i} - ", end="")
        print(*res, sep=", ")


if __name__ == "__main__":
    main()
