def main():
    n, m = [int(input()) for _ in range(2)]
    width = len(str(n * m))

    for i in range(n):
        for j in range(m):
            element = i * m + (j + 1 if i % 2 == 0 else m - j)
            print(f"{element}".rjust(width), end=" ")
        print()


if __name__ == "__main__":
    main()
