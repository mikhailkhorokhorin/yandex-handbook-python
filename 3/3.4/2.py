def main():
    l1, l2 = [input().split(", ") for _ in range(2)]
    print(*[f"{l1[i]} - {l2[i]}" for i in range(min(len(l1), len(l2)))], sep="\n")


if __name__ == "__main__":
    main()
