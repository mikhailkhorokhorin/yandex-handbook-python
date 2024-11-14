def main():
    input_files = input(), input()
    output_file = input()
    data = [set(), set()]
    for i in range(2):
        with open(input_files[i], "r") as file_in:
            for line in file_in:
                data[i].update({x for x in line.split()})

    with open(output_file, "w") as file_out:
        for word in sorted(data[0] ^ data[1]):
            print(word, file=file_out)


if __name__ == "__main__":
    main()
