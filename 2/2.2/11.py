number = input()
n = sorted([int(x) for x in number])
if n[2] + n[0] == n[1] * 2:
    print("YES")
else:
    print("NO")