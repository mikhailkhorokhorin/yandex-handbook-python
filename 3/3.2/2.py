# Символическая разница
def main() -> None:
    print(*(set(input()) & set(input())), sep="")


if __name__ == "__main__":
    main()
