def main() -> None:
    while (string := input()) != "":
        (
            print(string[: string.index("#") :] if "#" in string else string)
            if string[0] != "#"
            else ...
        )


if __name__ == "__main__":
    main()
