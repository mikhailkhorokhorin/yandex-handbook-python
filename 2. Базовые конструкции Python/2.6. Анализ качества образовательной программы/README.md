# 2.6. Анализ качества образовательной программы
### A. Считывание параметров для анализа
```python
def main() -> None:
    N, M, Q, cw, sw, hw, tw = map(int, input().split())
    print(M, N, cw, sw, hw, tw, Q, sep="\n")


if __name__ == "__main__":
    main()
```
### B. Рейтинг ученика
```python
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
```
### C. Анализ качества образовательной программы
```python
def main() -> None:
    N, M, Q, cw, sw, hw, tw = map(int, input().split())

    if N < 3 or M <= 0 or cw <= 0 or sw <= 0 or hw <= 0 or tw <= 0:
        print("Во введённых данных ошибка")
        return

    students = []

    for i in range(N):
        surname = input().strip()
        rating = 0

        for _ in range(M):
            a, b, c, d = map(int, input().strip().split(","))
            rating += a * cw + b * sw + c * hw + d * tw

        if rating > Q:
            print("Во введённых данных ошибка")
            return

        percent = round(rating / Q * 100)
        students.append((surname, rating, percent, i))

    max_p = max(p for _, _, p, _ in students)
    min_p = min(p for _, _, p, _ in students)
    avg_p = round(sum(r for _, r, _, _ in students) / (N * Q) * 100)

    print(max_p, avg_p, min_p)

    top3 = sorted(students, key=lambda x: (-x[1], x[3]))[:3]
    print(*(f"{s} {p}%" for s, _, p, _ in top3), sep="\n")
    print("Курс усваивается " + ("плохо" if avg_p <= 50 else "хорошо"))


if __name__ == "__main__":
    main()
```
