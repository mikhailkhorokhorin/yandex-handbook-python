def main() -> None:
    for index, product in enumerate(sorted({word for _ in range(3) for word in input().split(", ")})):
        print(f"{index + 1}. {product}")


if __name__ == "__main__":
    main()
