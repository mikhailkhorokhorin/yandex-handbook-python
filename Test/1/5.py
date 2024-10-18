def main():
    res = -100000000000000000
    for i in range(int(input())):
        nums = []
        while (s := input()) != "next":
            nums.append(int(s))
        res = max(res, sum(nums) / len(nums))

    print(f"{res:.2f}")


if __name__ == "__main__":
    main()
