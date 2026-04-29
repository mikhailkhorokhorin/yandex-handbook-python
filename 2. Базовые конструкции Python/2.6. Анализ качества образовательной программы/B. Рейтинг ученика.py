def main() -> None:
    data = input().split()
    N, M, Q, cw, sw, hw, tw = map(int, data)

    if M <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
        print("Во введённых данных ошибка")
        return

    surname = input()
    rating = 0

    for _ in range(M):
        a, b, c, d = map(int, input().split(","))
        rating += a * cw + b * sw + c * hw + d * tw

    if rating > Q:
        print("Во введённых данных ошибка")
        return

    percent = round(rating / Q * 100)
    print(f"{surname} {percent}%")


if __name__ == "__main__":
    main()
