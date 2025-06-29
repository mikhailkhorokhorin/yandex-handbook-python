def main() -> None:
    numbers, power = [int(input()) for _ in range(int(input()))], int(input())
    print(*[i**power for i in numbers], sep="\n")


if __name__ == "__main__":
    main()
