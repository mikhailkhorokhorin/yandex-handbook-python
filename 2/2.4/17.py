# А роза упала на лапу Азора 3.0
def main() -> None:
    print(sum([(string := input()) == string[::-1] for _ in range(int(input()))]))


if __name__ == "__main__":
    main()
