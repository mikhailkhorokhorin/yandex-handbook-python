# Зайка — 2
def main() -> None:
    result = min([i for i in ([input() for _ in range(3)]) if "зайка" in i])
    print(result, len(result))


if __name__ == "__main__":
    main()
