def main():
    operation = input().lower()
    a, b = [int(input()) for _ in range(2)]

    if "sum" in operation:
        print(a + b)
    elif "sub" in operation:
        print(a - b)
    elif "mult" in operation:
        print(a * b)
    elif "div" in operation:
        print(a // b)


if __name__ == "__main__":
    main()
