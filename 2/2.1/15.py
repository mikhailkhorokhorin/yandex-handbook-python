n = int(input())
m = int(input())
t = int(input())

hours = t // 60
m += t % 60

n = (n + hours + m // 60) % 24
m %= 60

print(f"{n if n >= 10 else f'0{n}'}:{m if m >= 10 else f'0{m}'}")
