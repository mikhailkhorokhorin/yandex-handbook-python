def main():
    line = input()
    letter, count = line[0], 1

    for i in line[1:]:
        if i == letter:
            count += 1
        else:
            print(letter, count)
            letter, count = i, 1
    print(letter, count)


if __name__ == "__main__":
    main()
