def main() -> None:
    headings, request = [input() for _ in range(int(input()))], input()
    print(*[i for i in headings if request.lower() in i.lower()], sep='\n')


if __name__ == "__main__":
    main()
