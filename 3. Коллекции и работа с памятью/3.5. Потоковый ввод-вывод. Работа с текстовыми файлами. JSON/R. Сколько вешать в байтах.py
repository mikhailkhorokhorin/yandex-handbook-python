import math
import os


def main() -> None:
    size, postfixes, index = (
        os.path.getsize(input()),
        ["Б", "КБ", "МБ", "ГБ"],
        0,
    )
    while size >= 1024 and index < len(postfixes) - 1:
        size = math.ceil(size / 1024)
        index += 1
    print(size, postfixes[index], sep="")


if __name__ == "__main__":
    main()
