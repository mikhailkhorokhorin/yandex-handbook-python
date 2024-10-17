def main():
    cords = [list(map(int, input().split())) for _ in range(int(input()))]
    res = 0
    n = 1
    for i in range(1, len(cords) + 1):
        if (cords[n][0] // 10) == (cords[n + 1][0] // 10) and abs((cords[n][0] % 10) - (cords[n + 1][0] % 10)) <= 9 and \
                (cords[n][1] // 10) == (cords[n + 1][1] // 10) and abs((cords[n][1] % 10) - (cords[n + 1][1] % 10)) <= 9:
            res += 1
        else:
            cords.remove(cords[n])
            n -= 1
    print(res)


if __name__ == "__main__":
    main()
