# Новогоднее настроение 2.0
def main() -> None:
    n = int(input())
    max_length, number, line = 0, 0, 1
    while number < n:
        length = " ".join(str(i) for i in range(number + 1, min(number + line + 1, n + 1)))
        max_length = max(len(length), max_length)
        number += line
        line += 1
    number, line = 0, 1
    while number < n:
        answer = " ".join(str(i) for i in range(number + 1, min(number + line + 1, n + 1)))
        print(f"{answer:^{max_length}}")
        number += line
        line += 1


if __name__ == "__main__":
    main()
