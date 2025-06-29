# 6.1. Модули math и numpy
### A. Математика — круто, но это не точно
```python
from math import log, pow, sin, cos, pi, e


def main() -> None:
    print(
        log(pow(x := float(input()), 3 / 16), 32)
        + pow(x, cos((pi * x) / (2 * e)))
        - pow(sin(x / pi), 2)
    )


if __name__ == "__main__":
    main()
```
### B. Потоковый НОД
```python
from math import gcd
from sys import stdin


def main() -> None:
    print(*[gcd(*map(int, i.split())) for i in stdin], sep="\n")


if __name__ == "__main__":
    main()
```
### C. Есть варианты
```python
from math import comb


def main() -> None:
    n, m = map(int, input().split())
    print(comb(n, m) * m // n, comb(n, m))


if __name__ == "__main__":
    main()
```
### D. Среднее не арифметическое
```python
from math import pow, prod


def main() -> None:
    numbers = list(map(float, input().split()))
    print(pow(prod(numbers), 1 / len(numbers)))


if __name__ == "__main__":
    main()
```
### E. Шаг навстречу
```python
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
```
### F. Матрица умножения
```python
import numpy as np


def multiplication_matrix(n) -> np.array:
    matrix = np.arange(1, n + 1)
    return matrix * matrix[:, None]
```
### G. Шахматная подготовка
```python
import numpy as np


def make_board(number: int) -> np.array:
    return np.array(
        np.rot90(np.indices((number, number)).sum(axis=0) % 2), dtype="int8"
    )
```
### H. Числовая змейка 3.0
```python
import numpy as np


def snake(m: int, n: int, direction: str = "H") -> np.array:
    matrix, num = np.zeros((n, m), dtype="int16"), 1
    for i in range(n if direction == "H" else m):
        if direction == "H":
            matrix[i] = (
                np.arange(num, num + m)
                if i % 2 == 0
                else np.arange(num + m - 1, num - 1, -1)
            )
        else:
            matrix[:, i] = (
                np.arange(num, num + n)
                if i % 2 == 0
                else np.arange(num + n - 1, num - 1, -1)
            )
        num += m if direction == "H" else n
    return matrix
```
### I. Вращение
```python
import numpy as np


def rotate(matrix: np.array, angle: int) -> np.array:
    return np.rot90(matrix, (360 - angle) // 90)
```
### J. Лесенка
```python
import numpy as np


def stairs(vector: np.array) -> np.array:
    return np.array([np.roll(vector, i) for i in range(len(vector))])
```
