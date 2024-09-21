def main():
    n = sorted([int(x) for x in input()])
    print("YES" if n[2] + n[0] == n[1] * 2 else "NO")


if __name__ == "__main__":
    main()
