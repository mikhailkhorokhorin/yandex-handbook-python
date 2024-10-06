def main():
    length = int(input())
    strings = [input() for _ in range(int(input()))]

    total = length
    for i in strings:
        if total <= 3:
            break
        print(i[:total:] if (total - len(i)) > 3 else i[:total - 3:] + "...")
        total -= len(i)


if __name__ == "__main__":
    main()
