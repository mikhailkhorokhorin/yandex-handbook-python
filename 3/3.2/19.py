# Частная собственность
def main() -> None:
    result = []
    for i in range(int(input())):
        result.extend(set(input().split(": ")[1].split(", ")))
    result = [x for x in result if result.count(x) == 1]
    print(*(sorted(result)), sep="\n")


if __name__ == "__main__":
    main()