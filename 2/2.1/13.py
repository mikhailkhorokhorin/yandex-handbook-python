def main():
    candies = int(input())
    in_bag = int(input())

    spended = in_bag // candies
    saved = in_bag % candies

    print(spended)
    print(saved)


if __name__ == "__main__":
    main()
