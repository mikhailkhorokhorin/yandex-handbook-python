def main():
    n = int(input())

    s1 = n % 10 + (n // 10) % 10
    s2 = n // 100 + (n // 10) % 10

    print(f"{s1}{s2}" if s1 >= s2 else f"{s2}{s1}")


if __name__ == "__main__":
    main()
