def main() -> None:
    side1, side2, side3 = [int(input()) for _ in range(3)]
    print(
        "YES"
        if (side1 < side2 + side3)
        and (side2 < side1 + side3)
        and (side3 < side1 + side2)
        else "NO"
    )


if __name__ == "__main__":
    main()
