def main():
    elements = list(input().split())
    res = []
    for i in elements:
        if i.isdigit():
            res.append(int(i))
        else:
            a = res.pop()
            exec("res[-1] " + i + "= a")
    print(*res)


if __name__ == "__main__":
    main()
