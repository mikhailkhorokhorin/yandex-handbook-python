def main():
    a, b, c = [float(input()) for _ in range(3)]

    if a == b == c == 0:
        print("Infinite solutions")
    elif a == b == 0:
        print("No solution")
    elif a == c == 0:
        print("0")
    elif a == 0 and b != 0:
        print(f"{-(c / b):.2f}")
    else:
        D = b ** 2 - 4 * a * c

        if D == 0:
            x = -b / 2 * a
            print(f"{x:.2f}")
        elif D > 0:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            print(f"{(min(x1, x2)):.2f}", f"{(max(x1, x2)):.2f}")
        else:
            print("No solution")


if __name__ == "__main__":
    main()
