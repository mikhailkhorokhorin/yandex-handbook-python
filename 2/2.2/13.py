def main():
    s1, s2, s3 = [int(input()) for _ in range(3)]
    print(s1 // 10 if (s1 // 10) == (s2 // 10) == (s3 // 10) else s1 % 10)


if __name__ == "__main__":
    main()
