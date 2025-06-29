def compare(numbers: list) -> int:
    odd = sum(1 for x in numbers if int(x) % 2 == 0)
    even = len(numbers) - odd
    return 0 if odd > even else 1 if odd < even else 2


def main() -> None:
    numbers, even, odd, eq = [input() for _ in range(4)]
    lines, k = [], 0
    with open(numbers, encoding="UTF-8") as file:
        for line in file:
            lines.append([x for x in line.split()])
    for t in even, odd, eq:
        with open(t, "w", encoding="UTF-8") as file:
            for i in range(len(lines)):
                for j in lines[i]:
                    if compare(j) == k:
                        print(j, end=" ", file=file)
                print("", file=file)
        k += 1


if __name__ == "__main__":
    main()
