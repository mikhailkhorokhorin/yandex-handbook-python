# Файловая разница
def main() -> None:
    input_files = [input() for _ in range(2)]
    output_file = input()
    data = [set(), set()]
    for i in range(2):
        with open(input_files[i], "r") as file:
            for line in file:
                data[i].update({x for x in line.split()})

    with open(output_file, "w") as file:
        for word in sorted(data[0] ^ data[1]):
            print(word, file=file)


if __name__ == "__main__":
    main()
