n = int(input())
m = int(input())
k = int(input())

d = {"Петя": n, "Вася": m, "Толя": k}
sorted_d = sorted(d.items(), key=lambda x: x[1])[::-1]

print("{:^24}".format(f"{sorted_d[0][0]}"))
print("{:^8}".format(f"{sorted_d[1][0]}"))
print(" " * 16 + "{:^8}".format(f"{sorted_d[2][0]}"))
print("{:^8}".format("II") + "{:^8}".format("I") + "{:^8}".format("III"))
