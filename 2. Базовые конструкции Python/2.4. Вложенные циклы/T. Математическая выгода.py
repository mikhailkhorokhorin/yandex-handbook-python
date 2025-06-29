def main() -> None:
    n = int(input())
    max_i = max_num = 0
    for i in range(2, 11):
        num, s = n, []
        while num > 0:
            s, num = [num % i] + s, num // i
        if max_num < sum(s):
            max_num, max_i = sum(s), i
    print(max_i)


if __name__ == "__main__":
    main()
