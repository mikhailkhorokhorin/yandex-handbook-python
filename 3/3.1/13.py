def main():
    numbers = [int(input()) for _ in range(int(input()))]
    power = int(input())

    for i in numbers:
        print(i ** power)


if __name__ == "__main__":
    main()
