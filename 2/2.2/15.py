def main():
    s1, s2 = input(), input()
    num = sorted([int(x) for x in (s1[0], s1[1], s2[0], s2[1])])
    print(f"{max(num)}{(sum(num) - max(num) - min(num)) % 10}{min(num)}")


if __name__ == "__main__":
    main()
