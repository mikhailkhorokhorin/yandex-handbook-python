def main() -> None:
    print("YES" if (string := input()) == string[::-1] else "NO")


if __name__ == "__main__":
    main()
