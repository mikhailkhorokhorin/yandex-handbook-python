def to_roman(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = [
        "M",
        "CM",
        "D",
        "CD",
        "C",
        "XC",
        "L",
        "XL",
        "X",
        "IX",
        "V",
        "IV",
        "I",
    ]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += sym[i]
            n -= val[i]
        i += 1
    return roman_num


def roman(a: int, b: int) -> str:
    a_roman = to_roman(a)
    b_roman = to_roman(b)
    sum_roman = to_roman(a + b)
    return f"{a_roman} + {b_roman} = {sum_roman}"
