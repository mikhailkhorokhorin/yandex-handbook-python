def main():
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))

    for i in range(n):
        for j in range(m):
            element = j * n + (i + 1 if j % 2 == 0 else n - i)
            print(f"{element}".rjust(width), end=" ")
        print()


if __name__ == "__main__":
    main()
