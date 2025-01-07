# Властелин Чисел: Две Башни
def main() -> None:
    number = input()
    raw_combinations = [number[i] + number[j] for i in range(len(number)) for j in range(len(number)) if i != j]
    combinations = sorted([int(i) for i in raw_combinations if i[0] != '0'])
    print(combinations[0], combinations[-1])


if __name__ == "__main__":
    main()
