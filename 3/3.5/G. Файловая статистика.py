def main() -> None:
    numbers = []
    with open(input(), "r") as file:
        for line in file:
            numbers.extend([int(x) for x in line.split()])
    statistics = [len(numbers), len([x for x in numbers if x > 0]), min(numbers), max(numbers), sum(numbers),
                  round(sum(numbers) / len(numbers), 2)]
    print(*statistics, sep="\n")


if __name__ == "__main__":
    main()
