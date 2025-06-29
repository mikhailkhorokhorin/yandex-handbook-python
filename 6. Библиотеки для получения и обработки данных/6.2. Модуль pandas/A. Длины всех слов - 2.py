from pandas import Series


def length_stats(text: str) -> Series:
    text = "".join(i for i in text if i.isalpha() or i == " ")
    words = sorted(set(text.lower().split()))
    return Series([len(i) for i in words], index=words)
