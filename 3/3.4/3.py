# Рациональная считалочка
from itertools import count, takewhile


def main() -> None:
    start, end, step = map(float, input().split())
    print(*[f'{value:.2f}' for value in takewhile(lambda x: x <= end, count(start, step))], sep='\n')


if __name__ == "__main__":
    main()
