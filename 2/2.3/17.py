num = input()
res = [int(x) for x in num if int(x) % 2 != 0]
print(*res, sep="")
