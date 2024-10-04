def main():
    n, m = [int(input()) for _ in range(2)]
    string = n * m + n - 1
    if n == 1:
        print(" " + str(n))
    else:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                print(f"{i * j:^{m}}", end="")
                if j == n:
                    print()
                else:
                    print("|", end="")
            if i != m:
                print("-" * string)


if __name__ == "__main__":
    main()
