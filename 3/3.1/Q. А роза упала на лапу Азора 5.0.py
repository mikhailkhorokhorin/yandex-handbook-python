def main() -> None:
    print(
        "YES" if (string := input().replace(" ", "").lower()) == string[::-1] else "NO"
    )


if __name__ == "__main__":
    main()
