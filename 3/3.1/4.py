# Очистка данных
def main() -> None:
    while (s := input()) != "":
        print(s[2::] if s[0:2:] == "##" else s) if s[-1:-4:-1] != "@@@" else ...


if __name__ == "__main__":
    main()
