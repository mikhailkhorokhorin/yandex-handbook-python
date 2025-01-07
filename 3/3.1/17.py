# А роза упала на лапу Азора 5.0
def main() -> None:
    print("YES" if (string := input().replace(" ", "").lower()) == string[::-1] else "NO")


if __name__ == "__main__":
    main()
