from math import dist, cos, sin


def main() -> None:
    deca = list(map(float, input().split()))
    pola = list(map(float, input().split()))
    print(
        dist(
            (deca[0], deca[1]),
            (pola[0] * cos(pola[1]), pola[0] * sin(pola[1])),
        )
    )


if __name__ == "__main__":
    main()
