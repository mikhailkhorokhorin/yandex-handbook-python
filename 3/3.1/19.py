# Польский калькулятор
def main() -> None:
    elements, result = list(input().split()), []
    for i in elements:
        if i.isdigit():
            result.append(int(i))
        else:
            a = result.pop()
            exec("result[-1] " + i + "= a")
    print(*result)


if __name__ == "__main__":
    main()
