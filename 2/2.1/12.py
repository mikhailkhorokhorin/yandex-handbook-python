def main():
    n, m = [int(input()) for _ in range(2)]

    s1 = (n // 100 + m // 100) % 10
    s2 = ((n // 10) % 10 + (m // 10) % 10) % 10
    s3 = (n % 10 + m % 10) % 10
    print(f"{s1}{s2}{s3}")


if __name__ == "__main__":
    main()
