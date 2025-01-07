# Массовое возведение в степень 2.0
def main() -> None:
    numbers, power = list(map(int, input().split())), int(input())
    print(*[i ** power for i in numbers])


if __name__ == "__main__":
    main()
