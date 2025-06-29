def main() -> None:
    result, hn = -1, 0
    for i in range(int(input())):
        b = int(input())
        h = b % 256
        r = (b // 256) % 256
        m = b // (256**2)
        temp = 37 * (hn + r + m) % 256
        if temp != h or h >= 100:
            result = i
            break
        hn = h
    print(result)


if __name__ == "__main__":
    main()
