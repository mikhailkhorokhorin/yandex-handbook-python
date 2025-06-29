from sys import stdin


def main() -> None:
    print(
        round(
            sum(
                x := [
                    int(line.split()[2]) - int(line.split()[1])
                    for line in stdin.readlines()
                ]
            )
            / len(x)
        )
    )


if __name__ == "__main__":
    main()
