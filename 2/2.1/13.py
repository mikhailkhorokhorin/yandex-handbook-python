def main():
    candies, in_bag = [int(input()) for _ in range(2)]

    spended = in_bag // candies
    saved = in_bag % candies

    print(spended, saved, sep="\n")


if __name__ == "__main__":
    main()
