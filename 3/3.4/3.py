from itertools import count


def main():
    start, end, step = list(map(float, input().split()))
    for value in count(start, step):
        if value <= end:
            print(f'{value:.2f}')
        else:
            break


if __name__ == "__main__":
    main()
