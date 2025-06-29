def main() -> None:
    result = []
    while string := input().split():
        if "зайка" in string:
            index = 0
            for i in range(string.count("зайка")):
                index = string.index("зайка", index + i)
                if index == 0 and len(string) > 1:
                    result.append(string[index + 1])
                elif index == (len(string) - 1):
                    result.append(string[index - 1])
                else:
                    result.append(string[index - 1])
                    result.append(string[index + 1])
    print(*set(result), sep="\n")


if __name__ == "__main__":
    main()
