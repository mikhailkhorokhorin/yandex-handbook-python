def compare(lst: list) -> int:
    odd = even = 0
    for x in lst:
        if int(x) % 2 == 0:
            odd += 1
        else:
            even += 1
    return 0 if odd > even else 1 if odd < even else 2


def main():
    nums, even, odd, d = [input() for _ in range(4)]
    list, k = [], 0
    with open(nums, encoding="UTF-8") as f_in:
        for line in f_in:
            list.append([x for x in line.split()])
    for t in even, odd, d:
        with open(t, "w", encoding="UTF-8") as f_out:
            for i in range(len(list)):
                for j in list[i]:
                    if compare(j) == k:
                        print(j, end=' ', file=f_out)
                print('', file=f_out)
        k += 1


if __name__ == "__main__":
    main()
