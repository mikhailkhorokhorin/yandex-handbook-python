# Редизайн таблицы умножения
def main() -> None:
    n, m = [int(input()) for _ in range(2)]
    string = m * n + (n - 1)
    if n != 1:
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                k = str(i * j)
                result = f'{k: ^{m}}'
                print(result, '|', sep="", end="") if j != n else print(result, end="")
            print()
            if i != n:
                print('-' * string)
    else:
        print(f"{1: ^{m}}")


if __name__ == "__main__":
    main()
