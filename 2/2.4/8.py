def main():
    d = {}
    for i in range(int(input())):
        name = input()
        d[name] = sum([int(x) for x in input()])
    sorted_d = sorted(d.items(), key=lambda x: x[1])[::-1]
    print(sorted_d[0][0])


if __name__ == "__main__":
    main()
