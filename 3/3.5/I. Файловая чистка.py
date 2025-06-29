def main() -> None:
    input_file, output_file = [input() for _ in range(2)]
    data = []
    with open(input_file, "r") as file:
        for line in file:
            data.append(line.strip().replace("\t", "").split())
    data = [x for x in data if any(x)]
    with open(output_file, "w") as file:
        for line in data:
            print(" ".join(line), file=file)


if __name__ == "__main__":
    main()
