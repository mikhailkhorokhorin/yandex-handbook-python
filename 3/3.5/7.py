def main():
    numbers = []
    with open(input(), "r") as file_in:
        for line in file_in:
            numbers.extend([int(x) for x in line.split()])
    print(len(numbers))
    print(len([x for x in numbers if x > 0]))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    print(round(sum(numbers) / len(numbers), 2))


if __name__ == "__main__":
    main()
