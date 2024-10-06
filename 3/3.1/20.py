def main():
    elements = list(input().split())
    res = []
    for i in elements:
        if i.isdigit():
            res.append(int(i))
        elif i == '~':
            res[-1] *= -1
        elif i == "!":
            res[-1] = f(res[-1])
        elif i == "#":
            res.append(res[-1])
        elif i == "/":
            a = res.pop()
            res[-1] //= a
        elif i == "@":
            a = res.pop(-3)
            res.append(a)
        else:
            a = res.pop()
            exec("res[-1] " + i + "=a")
    print(*res)


def f(n):
    return n * f(n - 1) if n > 1 else 1


if __name__ == "__main__":
    main()