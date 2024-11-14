from sys import stdin


def main():
    x = [i.strip() for i in stdin]
    print(*[line for line in x[:-1] if x[-1].lower() in line.lower()], sep="\n")


if __name__ == "__main__":
    main()
