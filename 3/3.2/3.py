def main():
    elements = []
    for _ in range(int(input())):
        elements.extend(input().split())
    print(*set(elements), sep="\n")


if __name__ == "__main__":
    main()
