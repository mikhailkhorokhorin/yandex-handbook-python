def main():
    while (s := input()) != "":
        if s[-1:-4:-1] != "@@@":
            print(s[2::] if s[0:2:] == "##" else s)


if __name__ == "__main__":
    main()
