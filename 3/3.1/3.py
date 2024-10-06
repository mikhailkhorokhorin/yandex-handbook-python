def main():
    n = int(input())
    for _ in range(int(input())):
        print(s[:n - 3:] + "..." if len(s := input()) > n else s)


if __name__ == "__main__":
    main()
