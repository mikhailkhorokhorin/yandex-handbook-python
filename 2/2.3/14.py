def main():
    def P(x):
        return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

    num = int(input())
    print("YES" if P(num) else "NO")


if __name__ == "__main__":
    main()
