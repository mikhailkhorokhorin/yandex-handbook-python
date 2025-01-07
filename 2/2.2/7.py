# А роза упала на лапу Азора
def main() -> None:
    print("YES" if (number := input()) == number[::-1] else "NO")


if __name__ == "__main__":
    main()
