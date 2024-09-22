def main():
    n = int(input())
    for i in range(n):
        for j in range(3 + i, 0, -1):
            print(f"До старта {j} секунд(ы)")
        print(f"Старт {i + 1}!!!")


if __name__ == "__main__":
    main()
