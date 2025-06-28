def main() -> None:
    a, b, c = [float(input()) for _ in range(3)]

    if a == b == c == 0:
        print("Infinite solutions")
    elif (a == b == 0 and c != 0) or b**2 < 4 * a * c:
        print("No solution")
    elif b**2 == 4 * a * c:
        print(f"{-b / (2 * a):.2f}")
    elif a == 0:
        print(f"{-c / b:.2f}")
    else:
        solutions = sorted(
            [
                (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a),
                (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a),
            ]
        )
        print(f"{solutions[0]:.2f} {solutions[1]:.2f}")


if __name__ == "__main__":
    main()
