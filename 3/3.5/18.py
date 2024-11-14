import os
import math


def main():
    size = os.path.getsize(input())
    postfixes = ["Б", "КБ", "МБ", "ГБ"]
    index = 0

    while size >= 1024 and index < len(postfixes) - 1:
        size = math.ceil(size / 1024)
        index += 1

    print(size, postfixes[index], sep="")


if __name__ == "__main__":
    main()
