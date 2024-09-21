def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


a = int(input())
b = int(input())

print(a * b // NOD(a, b))
