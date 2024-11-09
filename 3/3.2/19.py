def main():
    res = []
    for i in range(int(input())):
        a, b = input().split(": ")
        res.extend(set(b.split(", ")))
    res = [x for x in res if res.count(x) == 1]
    print(*(sorted(res)), sep="\n")


if __name__ == "__main__":
    main()
