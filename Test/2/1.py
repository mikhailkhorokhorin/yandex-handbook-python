def main():
    n = int(input())
    lines = [input() for _ in range(n)]
    for i in range(n):
        nums = lines[i].split("^")
        print(lines[i][int(nums[1]) : int(nums[2]) + 1 : len(nums[0]) % 4])


if __name__ == "__main__":
    main()
