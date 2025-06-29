# 6.2. Модуль pandas
### A. Длины всех слов - 2
```python
from pandas import Series


def length_stats(text: str) -> Series:
    text = "".join(i for i in text if i.isalpha() or i == " ")
    words = sorted(set(text.lower().split()))
    return Series([len(i) for i in words], index=words)
```
### B. Длины всех слов по чётности
```python
from pandas import Series


def length_stats(text: str) -> tuple[Series, Series]:
    text = "".join(i for i in text if i.isalpha() or i == " ")
    words = sorted(set(text.lower().split()))
    odd, even = [i for i in words if len(i) % 2], [
        i for i in words if not len(i) % 2
    ]
    return (
        Series([len(i) for i in odd], index=odd, dtype="int64"),
        Series([len(i) for i in even], index=even, dtype="int64"),
    )
```
### C. Чек - 2
```python
from pandas import DataFrame, Series


def cheque(price_list: Series, **kwargs) -> DataFrame:
    products = sorted(kwargs)
    product_dict = {
        "product": products,
        "price": [price_list[i] for i in products],
        "number": [kwargs[i] for i in products],
    }
    product_dict["cost"] = [
        price_list[i] * product_dict["number"][index]
        for index, i in enumerate(products)
    ]
    return DataFrame(product_dict)
```
### D. Акция
```python
from pandas import DataFrame, Series


def cheque(price_list: Series, **kwargs) -> DataFrame:
    products = sorted(kwargs)
    product_dict = {
        "product": products,
        "price": [price_list[i] for i in products],
        "number": [kwargs[i] for i in products],
    }
    product_dict["cost"] = [
        price_list[i] * product_dict["number"][index]
        for index, i in enumerate(products)
    ]
    return DataFrame(product_dict)


def discount(cheque: DataFrame) -> DataFrame:
    new_cheque = cheque.copy()
    for i in range(len(new_cheque.loc[:, "cost"])):
        new_cheque.loc[i, "cost"] /= 1 + (cheque.loc[:, "number"][i] > 2)
    return new_cheque
```
### E. Длинные слова
```python
from pandas import Series


def get_long(data: Series, min_length: int = 5) -> Series:
    return data[data >= min_length]
```
### F. Отчёт успеваемости
```python
from pandas import DataFrame


def best(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    return new_journal[
        (new_journal["maths"] > 3)
        & (new_journal["physics"] > 3)
        & (new_journal["computer science"] > 3)
    ]
```
### G. Отчёт неуспеваемости
```python
from pandas import DataFrame


def need_to_work_better(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    return new_journal[
        (new_journal["maths"] < 3)
        | (new_journal["physics"] < 3)
        | (new_journal["computer science"] < 3)
    ]
```
### H. Обновление журнала
```python
from pandas import DataFrame


def update(journal: DataFrame) -> DataFrame:
    new_journal = journal.copy()
    for i in range(len(new_journal.loc[:, "name"])):
        new_journal.loc[:, "average"] = (
            new_journal["maths"]
            + new_journal["physics"]
            + new_journal["computer science"]
        ) / 3
    return new_journal.sort_values(
        by=["average", "name"], ascending=(False, True)
    )
```
### I. Бесконечный морской бой
```python
from pandas import read_csv


def main() -> None:
    left_top, right_bottom = list(map(int, input().split())), list(
        map(int, input().split())
    )
    data = read_csv("data.csv")
    print(
        data[
            (left_top[0] <= data["x"])
            & (data["x"] <= right_bottom[0])
            & (right_bottom[1] <= data["y"])
            & (data["y"] <= left_top[1])
        ]
    )


if __name__ == "__main__":
    main()
```
### J. Экстремум функции
```python
from numpy import arange
from pandas import Series


def values(func, start: float, end: float, step: float) -> Series:
    index = arange(start, end + step, step)
    return Series(map(func, index), index=index, dtype="float64")


def min_extremum(data: Series) -> float:
    return min(data[data == min(data)].index)


def max_extremum(data: Series) -> float:
    return max(data[data == max(data)].index)
```
