def main():
    print("YES" if all(input()[0].upper() in "АБВ" for _ in range(int(input()))) else "NO")


if __name__ == "__main__":
    main()
