from sys import stdin


def main() -> None:
    print(*[i[0:i.find("#")] for i in stdin.readlines() if not i[0] == "#"], sep="\n")


if __name__ == "__main__":
    main()
