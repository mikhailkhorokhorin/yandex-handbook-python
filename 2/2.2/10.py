n = int(input())

s1 = n % 10 + (n // 10) % 10
s2 = n // 100 + (n // 10) % 10
if s1 >= s2:
    print(f"{s1}{s2}")
else:
    print(f"{s2}{s1}")
