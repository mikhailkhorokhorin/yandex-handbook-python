# Считалочка 2.0
def main() -> None:
    start, end = [int(input()) for _ in range(2)]
    step = 1 if start < end else -1
    print(*[i for i in range(start, end + step, step)], end=" ")


if __name__ == "__main__":
    main()
