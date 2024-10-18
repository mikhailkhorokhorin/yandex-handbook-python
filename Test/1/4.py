def main():
    nums = [int(input()) for _ in range(int(input()))]
    print(max([nums[i] for i in range(1, len(nums) - 1) if nums[i] < nums[i - 1]]))


if __name__ == "__main__":
    main()
