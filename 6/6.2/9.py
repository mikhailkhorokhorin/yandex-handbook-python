# Бесконечный морской бой
from pandas import read_csv


def main() -> None:
    left_top, right_bottom = list(map(int, input().split())), list(map(int, input().split()))
    data = read_csv("data.csv")
    print(data[(left_top[0] <= data["x"]) & (data["x"] <= right_bottom[0]) & (right_bottom[1] <= data["y"]) &
               (data["y"] <= left_top[1])])


if __name__ == "__main__":
    main()
