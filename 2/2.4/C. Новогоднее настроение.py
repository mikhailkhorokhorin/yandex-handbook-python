def main() -> None:
    number = 1
    for i in range(1, (n := int(input())) + 1):
        for j in range(i):
            if number - 1 < n:
                print(number, end=" ")
                number += 1
        print()


if __name__ == "__main__":
    main()
