def main():
    F, N = input(), int(input())
    data = []
    with open(F, 'r') as f:
        for line in f:
            data.append(line)
    for line in data[-N:]:
        print(line.strip())


if __name__ == "__main__":
    main()
