def main() -> None:
    print("А Б В")
    for i in range(1, (n := int(input())) + 1):
        print("\n".join(f"{i} {j} {n - i - j}" for j in range(1, n - i)))


if __name__ == "__main__":
    main()
