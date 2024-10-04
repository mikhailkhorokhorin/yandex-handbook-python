def main():
    n = int(input())
    max_i, max_num = 0, 0
    for i in range(2, 11):
        num = n
        s = []
        while num > 0:
            s = [num % i] + s
            num //= i
        if max_num < sum(s):
            max_num = sum(s)
            max_i = i
    print(max_i)


if __name__ == "__main__":
    main()
