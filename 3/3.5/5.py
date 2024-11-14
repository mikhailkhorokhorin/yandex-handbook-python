from sys import stdin


def main():
    data = [string.strip().split() for string in stdin]
    words = [word for line in data for word in line if word.lower() == word.lower()[::-1]]
    print(*sorted(set(words)), sep="\n")


if __name__ == "__main__":
    main()
