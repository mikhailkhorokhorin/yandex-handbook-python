def main():
    start, end = [int(input()) for _ in range(2)]
    step = 1 if start < end else -1
    for i in range(start, end + step, step):
        print(i, end=" ")


if __name__ == "__main__":
    main()
