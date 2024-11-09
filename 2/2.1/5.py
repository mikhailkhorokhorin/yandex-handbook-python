def main():
    coast, weight, money = [int(input()) for _ in range(3)]
    print(money - weight * coast)


if __name__ == "__main__":
    main()
