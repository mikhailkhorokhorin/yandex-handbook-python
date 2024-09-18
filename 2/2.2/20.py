s1 = input()
s2 = input()
s3 = input()

d = []
for i in (s1, s2, s3):
    if 'зайка' in i:
        d.append(i)

res = min(d)
print(res, len(res))