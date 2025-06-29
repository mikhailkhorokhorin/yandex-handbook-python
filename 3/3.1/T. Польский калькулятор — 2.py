def f(n: int) -> int:
    return n * f(n - 1) if n > 1 else 1


def main() -> None:
    elements = list(input().split())
    result = []
    for i in elements:
        if i.isdigit():
            result.append(int(i))
        elif i == "~":
            result[-1] *= -1
        elif i == "!":
            result[-1] = f(result[-1])
        elif i == "#":
            result.append(result[-1])
        elif i == "/":
            a = result.pop()
            result[-1] //= a
        elif i == "@":
            a = result.pop(-3)
            result.append(a)
        else:
            a = result.pop()
            exec("result[-1] " + i + "=a")
    print(*result)


if __name__ == "__main__":
    main()
