def main():
    res = {}
    for _ in range(int(input())):
        cords = input().split()
        if (x := f'{cords[0][:-1]}-{cords[1][:-1]}') in res:
            res[x] += 1
        else:
            res[x] = 1
    print(res)
    print(max(res.values()))


if __name__ == "__main__":
    main()
