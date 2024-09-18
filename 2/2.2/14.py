n = input()
h = [n[0] + n[1], n[0] + n[2], n[1] + n[0], n[1] + n[2], n[2] + n[0], n[2] + n[1]]
m = [int(x) for x in h if x[0] != '0']
print(min(m), max(m))
