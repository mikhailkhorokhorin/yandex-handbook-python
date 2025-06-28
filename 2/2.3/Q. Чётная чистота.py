def main() -> None:
    print(*[int(i) for i in input() if int(i) % 2 != 0], sep="")


if __name__ == "__main__":
    main()
