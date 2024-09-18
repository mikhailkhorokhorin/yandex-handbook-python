n = int(input())
m = int(input())
k = int(input())

d = {"Петя": n, "Вася": m, "Толя": k}
sorted_d = sorted(d.items(), key=lambda x: x[1])[::-1]

print(f"1. {sorted_d[0][0]}")
print(f"2. {sorted_d[1][0]}")
print(f"3. {sorted_d[2][0]}")
