def main():
    a, b, c = [int(input()) for _ in range(3)]
    print(f"{a} ^ ({b} mod {c}) = {a ** (b % c)}")


if __name__ == "__main__":
    main()
