def main():
    numbers = list(map(int, input().split()))
    power = int(input())

    for i in numbers:
        print(i ** power, end=" ")


if __name__ == "__main__":
    main()
