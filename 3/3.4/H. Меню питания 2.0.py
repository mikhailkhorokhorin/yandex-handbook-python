def main() -> None:
    n = int(input())
    porridge = [input() for _ in range(n)]
    print(*(porridge[i % n] for i in range(int(input()))), sep='\n')


if __name__ == "__main__":
    main()
