def main():
    headings = [input() for _ in range(int(input()))]
    request = input()

    for i in headings:
        if request.lower() in i.lower():
            print(i)


if __name__ == "__main__":
    main()
