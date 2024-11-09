def main():
    res, hn1 = -1, 0
    for i in range(int(input())):
        b = int(input())
        h = b % 256
        r = (b // 256) % 256
        m = b // (256 ** 2)
        temp = 37 * (hn1 + r + m) % 256
        if temp != h or h >= 100:
            res = i
            break
        hn1 = h
    print(res)


if __name__ == "__main__":
    main()
