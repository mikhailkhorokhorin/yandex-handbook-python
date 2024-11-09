def main():
    result = []
    while s := input().split():
        if "зайка" in s:
            ind = 0
            for i in range(s.count("зайка")):
                ind = s.index("зайка", ind + i)
                if ind == 0 and len(s) > 1:
                    result.append(s[ind + 1])
                elif ind == (len(s) - 1):
                    result.append(s[ind - 1])
                else:
                    result.append(s[ind - 1])
                    result.append(s[ind + 1])
    print(*set(result), sep="\n")


if __name__ == "__main__":
    main()
