def main():
    input_file, output_file = [input() for _ in range(2)]
    data = []
    with open(input_file, 'r') as file_in:
        for line in file_in:
            data.append(line.strip().replace('\t', '').split())
    data = [x for x in data if any(x)]
    with open(output_file, "w") as file_out:
        for line in data:
            print(' '.join(line), file=file_out)


if __name__ == "__main__":
    main()
