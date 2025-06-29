def main() -> None:
    print(
        *[
            max(int(i) for i in x)
            for x in [input() for _ in range(int(input()))]
        ],
        sep="",
    )


if __name__ == "__main__":
    main()
