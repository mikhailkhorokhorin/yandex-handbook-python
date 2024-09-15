n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

x = (m * n - n * k2) / (k1 - k2)
y = n - x
print(x, y)