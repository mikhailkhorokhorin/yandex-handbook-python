from math import log, pow, sin, cos, pi, e


def main() -> None:
    print(
        log(pow(x := float(input()), 3 / 16), 32)
        + pow(x, cos((pi * x) / (2 * e)))
        - pow(sin(x / pi), 2)
    )


if __name__ == "__main__":
    main()
