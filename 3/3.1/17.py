def main():
    print("YES" if (s := input().replace(" ", "").lower()) == s[::-1] else "NO")


if __name__ == "__main__":
    main()
