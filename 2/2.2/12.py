def main():
    s1, s2, s3 = [int(input()) for _ in range(3)]
    print("YES" if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2) else "NO")


if __name__ == "__main__":
    main()
