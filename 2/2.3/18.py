def main():
    n = int(input())
    d = []
    div = 2
    if n < 2:
        print(n)
    while n > 1:
        if n % div == 0:
            d.append(div)
            n //= div
        else:
            div += 1

    print(*d, sep=" * ")


if __name__ == "__main__":
    main()
