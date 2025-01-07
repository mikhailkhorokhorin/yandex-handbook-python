# Простая задача 4.0
def LCD(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        num1, num2 = (num1 % num2, num2) if num1 > num2 else (num1, num2 % num1)
    return num1 + num2


def main() -> None:
    string = sorted(set(map(int, input().split("; "))))
    result = {str(i): [] for i in string}
    for i in string:
        result[str(i)].extend(str(j) for j in string if i != j and LCD(i, j) == 1)
        if result[str(i)]:
            print(f"{i} - {', '.join(result[str(i)])}")


if __name__ == "__main__":
    main()
