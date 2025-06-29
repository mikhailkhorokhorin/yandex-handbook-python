from pandas import Series


def length_stats(text: str) -> tuple[Series, Series]:
    text = "".join(i for i in text if i.isalpha() or i == " ")
    words = sorted(set(text.lower().split()))
    odd, even = [i for i in words if len(i) % 2], [i for i in words if not len(i) % 2]
    return (
        Series([len(i) for i in odd], index=odd, dtype="int64"),
        Series([len(i) for i in even], index=even, dtype="int64"),
    )
