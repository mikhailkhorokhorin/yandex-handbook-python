def main() -> None:
    num1, num2 = input(), input()
    combinations = sorted(
        [int(x) for x in (num1[0], num1[1], num2[0], num2[1])]
    )
    print(
        f"{combinations[-1]}{(sum(combinations) - combinations[-1] - combinations[0]) % 10}{combinations[0]}"
    )


if __name__ == "__main__":
    main()
