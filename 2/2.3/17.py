def main():
    print(*[int(x) for x in input() if int(x) % 2 != 0], sep="")


if __name__ == "__main__":
    main()
