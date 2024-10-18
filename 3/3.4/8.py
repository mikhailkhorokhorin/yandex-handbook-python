def main():
    n = int(input())
    porridge = [input() for _ in range(n)]
    for i in range(int(input())):
        print(porridge[i % n])


if __name__ == "__main__":
    main()
